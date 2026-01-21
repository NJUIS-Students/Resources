import os
import re
import json
import time
from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document
from openai import OpenAI
from typing import Dict, Any, Optional

# 全局配置
OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = "qwen3-max"

def extract_info_from_pdf(file_path):
    """从PDF文件提取开头信息"""
    try:
        reader = PdfReader(file_path)
        if len(reader.pages) > 0:
            text = reader.pages[0].extract_text()
            # 只取前800个字符，给AI更多上下文
            return text[:800]
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return ""

def extract_info_from_docx(file_path):
    """从DOCX文件提取开头信息"""
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs[:15]:  # 取前15段
            text += paragraph.text + "\n"
            if len(text) > 800:
                break
        return text[:800]
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
    return ""

def get_file_info(file_path):
    """获取文件信息"""
    file_path = Path(file_path)
    if file_path.suffix.lower() == '.pdf':
        return extract_info_from_pdf(file_path)
    elif file_path.suffix.lower() in ['.doc', '.docx']:
        return extract_info_from_docx(file_path)
    return ""

def call_ai_api(file_name, text_content: str) -> Optional[Dict[str, Any]]:
    """调用AI API分析文档内容"""
    if not OPENAI_BASE_URL or not OPENAI_API_KEY:
        print("警告: 未设置 OPENAI_BASE_URL 或 OPENAI_API_KEY 环境变量")
        return None
    
    # 构建提示
    prompt = f"""你是一个文档分类专家。请分析以下考试文档的开头内容，返回严格的JSON格式结果。
文档名称：
"{file_name}"

文档开头内容：
"{text_content}"

请返回以下JSON格式：
{{
  "exam_type": "期中或期末",
  "semester": "学期信息，如'2023-2024学年第一学期'或'2023春季'，如果没有明确信息则为'未知学期'",
  "has_answer": "带答案或无答案",
  "confidence": "置信度分数(0-1)",
  "reasoning": "简要分析理由"
}}"""
    
    # 初始化OpenAI客户端
    try:
        client = OpenAI(
            base_url=OPENAI_BASE_URL,
            api_key=OPENAI_API_KEY
        )
    except Exception as e:
        print(f"初始化OpenAI客户端失败: {e}")
        return None
    
    # 重试机制
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=500
            )
            
            content = response.choices[0].message.content
            
            # 尝试解析JSON
            try:
                # 清理可能的Markdown代码块
                if content.startswith("```json"):
                    content = content[7:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()
                
                parsed_result = json.loads(content)
                return parsed_result
            except json.JSONDecodeError as e:
                print(f"AI返回的不是有效JSON: {e}")
                print(f"原始响应: {content}")
                continue
                
        except Exception as e:
            print(f"AI API调用异常 (尝试 {attempt + 1}/3): {e}")
            time.sleep(2 ** attempt)  # 指数退避
    
    return None

def manual_intervention(file_name: str, text_content: str, ai_result: Optional[Dict] = None) -> Dict[str, Any]:
    """人工介入处理"""
    print(f"\n{'='*60}")
    print(f"需要人工介入处理文件: {file_name}")
    print(f"{'='*60}")
    
    if text_content:
        print(f"\n文档开头内容:")
        print(f"{text_content[:300]}...")
    
    if ai_result:
        print(f"\nAI分析结果:")
        print(f"  考试类型: {ai_result.get('exam_type', 'N/A')}")
        print(f"  学期信息: {ai_result.get('semester', 'N/A')}")
        print(f"  答案状态: {ai_result.get('has_answer', 'N/A')}")
        print(f"  置信度: {ai_result.get('confidence', 'N/A')}")
        print(f"  分析理由: {ai_result.get('reasoning', 'N/A')}")
    
    print(f"\n请输入重命名信息 (按回车使用默认规则引擎):")
    
    exam_type = input("考试类型 (期中/期末) [默认: 期末]: ").strip()
    if not exam_type:
        exam_type = "期末"
    
    semester = input("学期信息 [默认: 未知学期]: ").strip()
    if not semester:
        semester = "未知学期"
    
    has_answer = input("答案状态 (带答案/无答案) [默认: 无答案]: ").strip()
    if not has_answer:
        has_answer = "无答案"
    
    return {
        "exam_type": exam_type,
        "semester": semester,
        "has_answer": has_answer,
        "confidence": 1.0,
        "reasoning": "人工介入"
    }

def fallback_rule_engine(text_content: str, file_name: str) -> Dict[str, Any]:
    """备选规则引擎"""
    exam_type = "期末"  # 默认为期末
    semester = "未知学期"
    has_answer = "无答案"
    
    # 检查是否包含期中
    if "期中" in text_content or "期中" in file_name:
        exam_type = "期中"
    
    # 检查年份和学期
    year_match = re.search(r'(\d{4})年', text_content + file_name)
    if year_match:
        year = year_match.group(1)
        # 检查是否有学年格式
        academic_year_match = re.search(r'(\d{4})-(\d{4})', text_content + file_name)
        if academic_year_match:
            semester = f"{academic_year_match.group(1)}-{academic_year_match.group(2)}"
        else:
            semester = year
        
        # 检查季节
        combined_text = text_content + file_name
        if "春季" in combined_text or "春" in combined_text:
            semester += "春季"
        elif "秋季" in combined_text or "秋" in combined_text:
            semester += "秋季"
    
    # 检查是否有答案
    combined_text = text_content + file_name
    if any(keyword in combined_text for keyword in ["答案", "参考答案", "解答", "-ans", "含答案", "ans"]):
        has_answer = "带答案"
    
    return {
        "exam_type": exam_type,
        "semester": semester,
        "has_answer": has_answer,
        "confidence": 0.5,
        "reasoning": "规则引擎备选方案"
    }

def process_file_with_ai(file_path: Path, output_dir: Path, force_manual: bool = False):
    """使用AI处理单个文件"""
    print(f"\n处理文件: {file_path.name}")
    
    # 提取文本信息
    text_content = get_file_info(file_path)
    if not text_content.strip():
        print(f"  无法读取文件内容，使用文件名分析")
        text_content = file_path.name
    
    # 显示开头内容（安全处理编码）
    try:
        preview = text_content[:100]
        print(f"  开头内容: {preview}...")
    except:
        print(f"  开头内容: 无法显示特殊字符")
    
    ai_result = None
    use_manual = force_manual
    
    if not force_manual:
        # 调用AI分析
        ai_result = call_ai_api(file_path.name, text_content)
        
        # 判断是否需要人工介入
        if ai_result is None:
            print("  AI分析失败，需要人工介入")
            use_manual = True
        elif isinstance(ai_result, dict):
            confidence = ai_result.get('confidence', 0)
            if confidence < 0.7:
                print(f"  AI置信度较低 ({confidence:.2f})，建议人工确认")
                confirm = input("  是否进行人工确认? (y/N): ").strip().lower()
                if confirm == 'y':
                    use_manual = True
            else:
                print(f"  AI分析成功，置信度: {confidence:.2f}")
        else:
            print("  AI返回格式错误，需要人工介入")
            use_manual = True
    
    # 人工介入或使用AI结果
    if use_manual:
        final_result = manual_intervention(file_path.name, text_content, ai_result)
    elif ai_result and isinstance(ai_result, dict):
        final_result = ai_result
    else:
        # 使用备选规则引擎
        print("  使用备选规则引擎")
        final_result = fallback_rule_engine(text_content, file_path.name)
    
    # 构建新文件名
    exam_type = final_result['exam_type']
    semester = final_result['semester']
    has_answer = final_result['has_answer']
    
    if has_answer == "带答案":
        new_name = f"{exam_type}-{semester}-带答案.pdf"
    else:
        new_name = f"{exam_type}-{semester}-无答案.pdf"
    
    # 处理重复文件名
    counter = 1
    final_name = new_name
    while (output_dir / final_name).exists():
        name_parts = new_name.rsplit('.', 1)
        final_name = f"{name_parts[0]}_{counter}.{name_parts[1]}"
        counter += 1
    
    new_path = output_dir / final_name
    
    # 文件操作
    try:
        if file_path.suffix.lower() in ['.doc', '.docx']:
            # 尝试转换Word到PDF
            try:
                from docx2pdf import convert
                temp_pdf_path = output_dir / f"{file_path.stem}_temp.pdf"
                convert(str(file_path), str(temp_pdf_path))
                if temp_pdf_path.exists():
                    temp_pdf_path.rename(new_path)
                else:
                    # 转换失败，直接复制
                    import shutil
                    shutil.copy2(file_path, new_path)
                    # 修改扩展名为.pdf
                    if new_path.suffix.lower() != '.pdf':
                        new_path = new_path.with_suffix('.pdf')
            except ImportError:
                # 没有安装docx2pdf，直接复制并改扩展名
                import shutil
                shutil.copy2(file_path, new_path)
                if new_path.suffix.lower() != '.pdf':
                    new_path = new_path.with_suffix('.pdf')
        else:
            # PDF文件直接复制
            import shutil
            shutil.copy2(file_path, new_path)
        
        print(f"  重命名为: {final_name}")
        print(f"  分析理由: {final_result.get('reasoning', 'N/A')}")
        
    except Exception as e:
        print(f"  文件操作失败: {e}")

def main():
    # 检查环境变量
    if not OPENAI_BASE_URL or not OPENAI_API_KEY:
        print("警告: 未设置 OPENAI_BASE_URL 或 OPENAI_API_KEY 环境变量")
        print("将使用规则引擎作为主要分析方法，AI功能不可用")
    
    # 创建输出目录
    base_dir = Path("离散数学/试卷")
    output_dir = Path("离散数学/试卷/重命名_AI")
    output_dir.mkdir(exist_ok=True)
    
    # 收集所有文件
    files = []
    for ext in ['*.pdf', '*.doc', '*.docx']:
        files.extend(base_dir.rglob(ext))
    
    # 过滤掉重命名目录中的文件
    files = [f for f in files if "重命名" not in str(f)]
    
    if not files:
        print("未找到需要处理的文件")
        return
    
    print(f"找到 {len(files)} 个文件需要处理")
    
    # 询问是否强制人工介入（处理EOFError）
    try:
        force_manual_input = input("是否对所有文件进行人工确认? (y/N): ").strip().lower()
        force_manual = force_manual_input == 'y'
    except (EOFError, KeyboardInterrupt):
        print("无法读取输入，默认不进行人工确认")
        force_manual = False
    
    # 处理每个文件
    processed_count = 0
    for file_path in files:
        try:
            process_file_with_ai(file_path, output_dir, force_manual)
            processed_count += 1
        except KeyboardInterrupt:
            print("\n用户中断处理")
            break
        except Exception as e:
            print(f"处理文件 {file_path.name} 时发生错误: {e}")
    
    print(f"\n处理完成! 成功处理 {processed_count}/{len(files)} 个文件")
    print(f"重命名后的文件保存在: {output_dir}")

if __name__ == "__main__":
    main()