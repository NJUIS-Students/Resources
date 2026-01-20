## 第六次作业
### 1. 证明以下几组 FOL 公理均是有效的

#### 第三组公理: $\vDash \forall(\alpha \rightarrow \beta) \rightarrow(\forall x \alpha \rightarrow \forall x \beta)$

$\Leftrightarrow$ 对于任意结构 $\mathfrak{A}$ 和赋值 $s$ 有 $\vDash_{\mathfrak{A}}(\forall x(\alpha \rightarrow \beta) \rightarrow(\forall x \alpha \rightarrow \forall x \beta))[s]$
$\Leftrightarrow$ 对于任意结构 $\mathfrak{A}$ 和赋值 $s$ 有 $\vDash_{\mathfrak{A}}(\forall x(\alpha \rightarrow \beta))\left[s\right.$ 蕴含 $\vDash_{\mathfrak{A}}(\forall x \alpha \rightarrow \forall x \beta)[s]$
$\Leftrightarrow$ 对于任意结构 $\mathfrak{A}$ 和赋值 $s$ 有 对任意 $d \in|\mathfrak{A}|$ 有 $\vDash_{\mathfrak{A  }}(\alpha \rightarrow \beta)\left[s(x \mid d)\right.$ 蕴含含 $\vDash_{\mathfrak{A  }}(\alpha \rightarrow \beta)[s(x \mid d)]$

同理可得 $\vDash_{\mathfrak{A}} \forall x \alpha[s(x \mid d)]$，根据 $\rightarrow$ 的语义，有 $\vDash_{\mathfrak{A}} \forall x(\alpha \rightarrow \beta)[s(x \mid d)]$ 成立当且仅当 $\nvdash_{\mathfrak{A}} \forall x \alpha[s(x \mid d)]$ 或 $\vDash_{\mathfrak{A}} \forall x \beta[s(x \mid d)]$ ，又由此时 $\vDash_{\mathfrak{A}} \forall x \alpha[s(x \mid d)]$ ，故有 $\vDash_{\mathfrak{A}} \forall x \beta[s(x \mid d)]$ 成立，即有 $\vDash \forall x \beta$ 成立。

因此 $\vDash \forall x(\alpha \rightarrow \beta) \rightarrow(\forall x \alpha \rightarrow \forall x \beta)$ 成立。

#### 第四组公理： $\vDash \alpha \rightarrow \forall x \alpha$, 其中 $x$ 不在 $\alpha$ 中自由出现

对于任意结构 $\mathfrak{A}$ 和任意赋值 $s$ ，假设 $\vDash_{\mathfrak{A}} \alpha[s]$ ，只需要证明 $\vDash_{\mathfrak{A}} \forall x \alpha[s]$ 。

而对于任意结构 $\mathfrak{A}$ 和任意赋值 $s ,~\vDash_{\mathfrak{A}} \alpha[s]$
$\Leftrightarrow$ 对于任意结构 $\mathfrak{A}$ 和任意赋值 $s$ 有：对任意 $d \in|\mathfrak{A}|$ 有 $\vDash_{\mathfrak{A}} \alpha[s(x \mid d)]$
$\Leftrightarrow$ 对于任意结构 $\mathfrak{A}$ 和任意赋值 $s$ 有： $\vDash_{\mathfrak{A}} \forall x \alpha[s]$ ，即 $\vDash \forall x \alpha$ 成立。

因此有 $\vDash \alpha \rightarrow \forall x \alpha$ 成立。


#### 第五组公理： $\vDash x=x$

对任意结构 $\mathfrak{A}$ 和任意赋值 $s$ ，均有 $\bar{s}(x)=\bar{s}(x)$ ，又根据原子公式的解释，可得 $\vDash_{\mathfrak{A}} x=x$，故有 $\vDash_{\mathfrak{A}} x=x$ 成立。由于结构 $\mathfrak{A}$ 是任意的，则有 $\vDash x=x$ 成立。

#### 第六组公理：$\models (x=y) \rightarrow (\alpha \rightarrow \alpha')$ ，其中 $\alpha$ 为原子公式，$\alpha'$ 为对 $\alpha$ 中的 $x$ 进行 $0$ 次或多次替换后得到的wff

依据[Enderton, pp.99]，只需证明 $\{x=y, \alpha\} \models \alpha'$

先证明引理：

**引理**：对于任意结构 $\mathfrak{A}$ 与赋值 $s$，若 $\models_{\mathfrak{A}} (x=y)[s]$，即 $s(x) = s(y)$，那么对任意项 $t$ ，若 $t'$ 是对 $t$ 中的 $x$ 进行 $0$ 次或多次替换得到的，那么有 $\bar{s}(t) = \bar{s}(t')$.

证明：对 $t$ 进行归纳

1. $t$ 是常量，则 $t$ 不含 $x$ ，显然成立.
2. $t$ 是变量 $x$，$\bar{s}(t)=\bar{s}(x)=s(x)=s(y)=\bar{s}(t')$.
3. $t$ 是 $n$ 元函数 $f(a_1, \dots, a_n)$，$\bar{s}(t)=\bar{s}(f(a_1,\dots,a_n))=f^{\mathfrak{A}}(\bar{s}(a_1,\dots, a_n))=f^{\mathfrak{A}}(\bar{s}(a_1',\dots, a_n'))= \bar{s}(t')$

引理得证。

下对原子公式 $\alpha$ 的情况进行讨论。

1. $\alpha$ 为 $t_1=t_2$，则 $\models_{\mathfrak{A}}\alpha \Leftrightarrow \bar{s}(t_1)=\bar{s}(t_2) \Leftrightarrow \bar{s}(t_1')=\bar{s}(t_2') \Leftrightarrow \models_{\mathfrak{A}} \alpha'$
2. $\alpha$ 为 $n$ 元谓词 $P(t_1, \dots, t_n)$，则 $\models_{\mathfrak{A}}\alpha[s] \Leftrightarrow (\bar{s}(t_1), \dots,\bar{s}(t_n)) \in P^{\mathfrak{A}} \Leftrightarrow (\bar{s}(t_1'), \dots, \bar{s}(t_n'))\in P^{\mathfrak{A}} \Leftrightarrow \models_{\mathfrak{A}} \alpha'[s]$

因此，第六组公理是有效的。

### 2. 证明FOL可靠性定理的推论2.31：若 $\Gamma$ 是可满足的，那么它是一致的

证明：

由 $\Gamma$ 是可满足的，知存在结构 $\mathfrak{A}$ 与赋值 $s$ 使得 $\models_{\mathfrak{A}}\Gamma[s]$. 假设 $\Gamma$ 不是一致的，则存在 wff $\alpha$ 使得 $\Gamma \vdash \alpha$ 且 $\Gamma \vdash \neg\alpha$. 由可靠性定理，可知 $\Gamma \models \alpha$ 且 $\Gamma \models \neg\alpha$，由语义蕴含的定义，可知 $\Gamma \models_{\mathfrak{A}} \alpha[s]$ 且 $\Gamma \models_{\mathfrak{A}} \neg\alpha[s]$，即 $\Gamma \models_{\mathfrak{A}} \alpha[s]$ 且 $\Gamma \not\models_{\mathfrak{A}}\alpha[s]$。 矛盾！原命题得证。

### 3. 证明：$P$ 为二元谓词，$f$ 为一元函数，证明：$\vDash x=y \rightarrow (Pzfx \rightarrow Pzfy)$

即证明：
对任意 $\mathfrak{U}$ 和赋值 $s$ 有 $\vDash_\mathfrak{U} (x=y)[s]$ 蕴含 $\vDash_\mathfrak{U} (Pzfx \rightarrow Pzfy)[s]$ 
$\Leftrightarrow$ 对任意 $\mathfrak{U}$ 和赋值 $s$ 有 $\vDash_\mathfrak{U} (x=y)[s]$ 和 $\vDash_\mathfrak{U} Pzfx[s]$ 蕴含 $\vDash_\mathfrak{U} Pzfy[s]$ 

由$\vDash_\mathfrak{U} Pzfx[s]$ 和对项的解释得，对任意 $\mathfrak{U}$ 和赋值 $s$ ：
 $(s(z),s(fx)) \in P^{\mathfrak{U}} \Leftrightarrow (s(z),f^{\mathfrak{U}}s(x)) \in P^{\mathfrak{U}}$

由$\vDash_\mathfrak{U} (x=y)[s]$ 得，对任意 $\mathfrak{U}$ 和赋值 $s$ ：
$(s(z),f^{\mathfrak{U}}s(y)) \in P^{\mathfrak{U}}$
即：$\vDash_\mathfrak{U} Pzfy[s]$ 

得证
  
### 4. 证明以下一阶逻辑公式不是逻辑有效的，但是可满足的，其中 $P$ 为二元谓词 $$\forall x(\neg Pxx)\wedge\forall x\forall y\forall z((Pxy\wedge Pyz)\rightarrow(Pxz\wedge\forall x \exists yPxy))$$
1. 证明不是逻辑有效的：
   令 $D \in \mathfrak{U}$ 中 $D = \{N,> \}$ ，$Pxy$ 为 $x > y$
   则显然$\forall x(\neg Pxx)$ 与 $\forall x\forall y\forall z((Pxy\wedge Pyz)$ 成立，但 $(Pxz\wedge\forall x \exists yPxy)$ 不一定成立

2. 证明可满足的：
   令 $D \in \mathfrak{U}$ 中 $D = \{N,< \}$ ，$Pxy$ 为 $x < y$
   则上式显然成立




