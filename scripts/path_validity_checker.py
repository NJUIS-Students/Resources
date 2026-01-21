import re
import sys
from pathlib import Path

def checker(file_path:str) -> tuple[bool, str]:
    splitted_path = file_path.split('/')

    if len(splitted_path) < 2 or splitted_path[0] in ['.git', '.github', 'script']:
        return True, '跳过'
    
    if splitted_path[1] == '试卷':
        # 课程名称/试卷/(期中|期末)-(xxxx-xxxx学年第x学期)-(带答案|无答案|回忆版)
        exam_pattern1 = r'^[^/]+/试卷/(期中|期末)-\d{4}-\d{4}学年第(一|二)学期'
        if re.match(exam_pattern1, splitted_path[-1]):
            return True, "试卷"
        # 课程名称/试卷/(期中|期末)-(xx级)-(带答案|无答案|回忆版)
        exam_pattern2 = r'^[^/]+/试卷/(期中|期末)-([0-9\-])级'
        if re.match(exam_pattern2, splitted_path[-1]):
            return True, "试卷"
        return False, f'试卷命名 {splitted_path[-1]} 不符合规范'
    elif splitted_path[1] == '笔记':
        return True, '课程笔记'
    elif re.match(r'\d{4}(春|秋)'):
        if len(splitted_path) == 3:
            return True, '文件'
        if re.match(r'^[^/]+/[^/]+/[^/]+/(课件|作业)', file_path) is None:
            return False, '课件/作业文件夹命名不符合命名规范'
        if splitted_path[3] == '课件':
            if re.match(r'\d{2}-[^/]+', splitted_path[-1]):
                return False, f'课件命名 {splitted_path[-1]} 不符合规范'
            else:
                return True, '课件'
        if splitted_path[3] == '作业':
            return True, '作业'
    elif len(splitted_path) == 2:
        return True, '文件'
    else:
        return False, f'二级目录 {splitted_path[1]} 不符合命名规范'

def main():
    # 从命令行参数读取所有变更文件路径
    if len(sys.argv) < 2:
        print("Usage: check_paths.py <file1> <file2> ...")
        sys.exit(status=0)  # 即使无参数也不报错，避免中断 CI

    invalid_files = []

    for path_str in sys.argv[1:]:
        full_path = Path(path_str)

        # 忽略已删除的文件
        if not full_path.exists():
            continue

        is_valid, reason = checker(path_str.replace("\\", "/"))  # 统一路径分隔符
        if not is_valid:
            invalid_files.append((path_str, reason))

    # 输出警告信息
    if invalid_files:
        print("\n❌ Invalid file paths detected:")
        for f, r in invalid_files:
            print(f"  - {f} ({r})")

        # 使用 GitHub warning 命令发送警告（不会导致失败）
        print("\n::warning title=Invalid File Paths::Some files do not follow the required structure.")
        print("Please refer to the contribution guide.")
    else:
        print("🎉 All file paths are valid!")

if __name__ == "__main__":
    main()