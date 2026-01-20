---
南京大学（苏州校区） 数理逻辑（2024春）任课教师：戴望州 课程主页： https://daiwz.net/teaching/
---

# 作业 - 01（参考答案）



### 1 形式化

用命题逻辑形式化以下推理，并指出哪些步骤是逻辑上非有效的：

1. 鱼越大, 鱼刺越大
2. 鱼刺越大，鱼肉越少
3. 鱼肉越少, 鱼越小
4. So：鱼越大，鱼越小

【解析】1、2、3都不是有效的（可构造反例）



### 2 证明

(Enderton, Ex 1.1.2 ) 不存在长度为 2,3 或 6 的 wff, 但其他任意正整数长度的 wff 均可能存在。

【解析】注意到，一个合式公式（wff）可以是单个命题符号（1个符号），另一个合式公式的否定（n+3个符号），或者使用某个二元连接符号的两个合式公式的组合（n+m+3个符号），其中 n 和 m 分别是所使用的合式公式中的符号数。因此，一个合式公式可以有**1**、1+3=**4**、4+3=**7**、1+1+3=**5**、1+4+3=**8**、1+5+3=**9** 个符号，进一步可能产生 k+3l 个符号，其中 k∈{7,8,9}，l∈N 。2 和 3 个符号是不可能的，因为 n+3 和 n+m+3 必然大于3。6 也不可能，否则就会导致 6=n+3，意味着 n=3；或者 6=n+m+3，意味着 n+m=3，即 n 或 m 等于2。



### 3 证明

(Enderton, Ex 1.1.3 ) 令 $\alpha$ 是一个 wff; 设 $c$ 为二元联词 $(\wedge, \vee, \rightarrow, \leftrightarrow)$ 在 $\alpha$ 中出现的次数, $s$ 是命题符号 $\left(\left\{\mathbf{A}_i, \ldots\right\}\right)$ 在 $\alpha$ 中出现的次数 (例如, 若 $\alpha$ 是 $(\mathbf{A} \rightarrow(\neg \mathbf{A}))$, 则 $\left.c=1, s=2\right)$ 。使用归纳法证明 $s=c+1$ 。

【解析】证明：只包含一个命题符号的 wff 包含$s=1$个命题符号，并且包含$c=0$个二元联词。假设$\alpha$和$\beta$分别是包含$n$和$m$个命题符号的wff，并且其对应的二元联词的个数分别为$n-1$和$m-1$。显然，$\alpha$的否定形式$\neg \alpha$并不会影响命题符号和二元联词的数量，并且，对于任意的wff $\alpha \star \beta$（$\star$任意的二元联词）包含$n+m$个命题符号和$n-1+1+m-1=n+m-1$个二元联词。依据归纳原则即可得出结论。



### 4 证明

令 $S^{\prime}=\left\{\alpha \mid\right.$ 存在有穷构造序列 $\left\langle\alpha_0, \alpha_1, \ldots, \alpha_n\right\rangle$ 使得 $\alpha_n=\alpha$ 且对任意 $i \leq n$ 满足定义 1.4 的 3 个条件之一 $\}$,证明 $S^{\prime}=S$ 。( $S$ 由定义 1.2 给出 $)$

【解析】

引理1.14. $A \in P R O P$ 等价于存在有穷序列 $A_0, A_1, \ldots, A_n$ 使得 $A=A_n$ 且对于 $\forall i \leq n$,

或(a) $A_i \in P S$ 

或(b) $\exists k<i$ 使 $A_i$ 为 $\left(\neg A_k\right)$

或(c) $\exists k, l<i$ 使 $A_i$ 为 $\left(A_k * A_l\right)$, 其中 $* \in\{\wedge, \vee, \rightarrow$ \}

以上序列 $A_0, A_1, \ldots, A_n$ 被称为 $\mathrm{A}$ 的构造序列。

证明：

令 $P R O P^{\prime}=\left\{A \mid\right.$ 存在有穷序列 $A_0, A_1, \ldots, A_n$ 使 $A_n$ 为 $A$ 且对任何 $i \leq n$ 或 $(a)$ 或 $(b)$ 或 $(c)\}$ 。

欲证 $P R O P=P R O P^{\prime}$，只需证 (1) $P R O P \subseteq P R O P^{\prime}$ 和 (2) $P R O P^{\prime} \subseteq PROP$ 

**现证 (1)**

设 $A \in P R O P^{\prime}$, 从而存在 $A_0, A_1, \ldots, A_n$ 满足对任何 $i \leq n$ 有 (a) 或 (b) 或 (c)。对 $i$ 归纳证明 $A_i \in P R O P$。

- 归纳基础：当 $i=0$ 时, 只有 (a) 成立, 即 $A_0 \in P S$ 。
- 归纳假设：设对于 $\forall k<i$ 有 $A_k \in P R O P$ 成立。
- 归纳步骤：对于 $i$ 有如下情况：

(a) $A_i \in P S$ 从而 $A_i \in P R O P$

(b) $A_i=\left(\neg A_k\right)$, 此处 $k<i$, 由归纳假设可知 $A_k \in$ $P R O P$ 

由形成规则 (ii)，可得 $A_i \in P R O P$  

(c) $A_i=\left(A_k * A_l\right)$，此时 $k, l<i$，从而有归纳假设可知：

$A_k, A_l \in P R O P$，由形成规则 (iii)，可得 $A_i \in$ $P R O P$  

由数学归纳法, 可得 $A_n \in P R O P, P R O P^{\prime} \subseteq P R O P$  

**现证 (2)**

由定义1.10可知，$P R O P$ 是满足定义 1.10 中条件 (i) (iii) 的最小集合，故只需证 $P R O P^{\prime}$ 也满足条件 (i) (iii)。

(i) $P S \subseteq P R O P^{\prime}$ 是显然的；
(ii) 设 $A \in P R O P^{\prime}$, 则存在 $\mathrm{A}$ 的构造序列 $A_0, A_1, \ldots, A_n$，那么
$$
A_0, A_1, \ldots, A_n,(\neg A)
$$

是 $(\neg A)$ 的构造序列, 因此 $(\neg A) \in P R O P^{\prime}$；

(iii) 类似地，设 $A, B \in P R O P^{\prime}$, 则存在 $\mathrm{A}$ 和 $\mathrm{B}$ 的构造序列，
$$
\begin{gathered}
A_0, A_1, \ldots, A_n \text { 和 } B_0, B_1, \ldots, B_n, \text { 那么 } \\
A_0, A_1, \ldots, A_n, B_0, B_1, \ldots, B_n,(A * B)
\end{gathered}
$$

是 $(A * B)$ 的构造序列，因此 $(A * B) \in P R O P^{\prime}$ 。

所以 $P R O P^{\prime}$ 也满足条件(i) (iii)，故 $P R O P \subseteq P R O P^{\prime}$ 。
