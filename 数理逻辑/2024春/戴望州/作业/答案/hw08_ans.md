## 第八次作业
### 2.1.1 命题逻辑程序的证明系统拥有可靠性吗？请证明你的结论

即证明 
$$F_1, \dots, F_n \vdash g_1, \dots,g_m \text{ implies } F_1, \dots, F_n \models g_1 \wedge \dots \wedge g_m$$

令 $\mathcal{I}$ 是一个解释，且满足 
$$\mathcal{I} \models F_1 \text{ and } \dots \text{ and } \mathcal{I} \models F_n$$ 

我们需要证明 $\mathcal{I} \models g_1 \wedge \dots \wedge g_m$

令 $\Pi$ 是 $g_1, \dots ,g_m$ 的推导树 (derivation tree)，我们将会证明对于所有出现在 $\Pi$ 中的目标 $g_1', \dots, g_{m'}'，$ $\mathcal{I} \models g_1' \wedge \dots \wedge g_{m'}'$ 成立。因此，特别地， $\mathcal{I} \models g_1 \wedge \dots \wedge g_m$成立。

**目标**：  对于所有出现在 $\Pi$ 中的目标 $g_1', \dots, g_{m'}'，$ $\mathcal{I} \models g_1' \wedge \dots \wedge g_{m'}'$ 成立。

证明：

分两种情况讨论：

1）如果 $g_1',\dots, g_{m'}'$ 是公理，那么 $m'=1$ 且 $g_1'$ 必然是 $F_1, \dots, F_n$ 其中之一。因此， 根据假设，$\mathcal{I} \models q$ 是显然的。

2）否则，在 $\Pi$ 推导出的 $g_1', \dots, g_{m'}'$ 一定具有如下形式：

$$ \frac{g_1', \dots, g_{l-1}',h_1, \dots, h_k,g_{l+1}',\dots, g_{m'}' \qquad h_1\wedge \dots \wedge h_k \rightarrow g_l'}{g_1', \dots, g_{m'}'}$$

其中，$h_1\wedge \dots \wedge h_k \rightarrow g_l'$ 是公理。

根据在树中传播的性质，

$$ \mathcal{I} \models g_1' \wedge \dots \wedge g_{l-1}' \wedge h_1 \wedge \dots \wedge h_k \wedge g_{l+1}' \wedge \dots \wedge g_{m'}'$$

由于$h_1\wedge \dots \wedge h_k \rightarrow g_l'$ 是公理，

$$ \mathcal{I} \models h_1 \wedge \dots \wedge h_k \rightarrow g_l'$$

因此， $\mathcal{I} \models g_1' \wedge \dots \wedge g_{m'}'$ 成立。

综上所述，可靠性得证。

### 2.1.2 命题逻辑程序的证明系统的完备性

即证明 

$$F_1, \dots, F_n \models q_1 \wedge \dots \wedge q_m \text{ implies } F_1, \dots, F_n \vdash q_1, \dots, q_m$$

定义如下解释 $\mathcal{I}$：

$$
\mathcal{I}(q) = \left\{
    \begin{array}{ll}
    \mathbf{true} & \text{if } F_1,\dots,F_n \vdash q\\
    \mathbf{false} & \text{otherwise}
    \end{array}
\right.
$$

接下来我们需要证明：

$$\mathcal{I} \models F_1 \text{ and } \dots \text{ and } \mathcal{I} \models F_n$$

分两种情况讨论：

1）如果 $F_i$ 是原子命题 $q$ 那么显然 $F_1, \dots, F_n \vdash q$，所以 $\mathcal{I}(q) =\mathbf{true} $，$\mathcal{I} \models q$

2）假设 $F_i$ 是一个蕴含式 $p_1 \wedge \dots \wedge p_k \rightarrow q$，我们需要证明 $\mathcal{I} \models p_1 \wedge \dots \wedge p_k \rightarrow q$：

假设 $\mathcal{I} \models p_1 \text{ and } \dots \text{ and } \mathcal{I} \models p_k$，即 $F_1, \dots, F_n \vdash p_1 \text{ and } \dots \text{ and } F_1, \dots, F_n \vdash p_k$，进行如下操作：

$$\frac{\frac{p_1 \quad \dots \quad p_k}{p_1, \dots, p_k} \qquad p_1 \wedge \dots \wedge p_k \rightarrow q}{q}$$

故 $F_1, \dots, F_n \vdash q$，因此 $\mathcal{I} \models q$.

现在，我们已经假设 $F_1, \dots, F_n \models q_1 \wedge \dots \wedge q_m$，而且我们已经证明 $\mathcal{I} \models F_1 \text{ and } \dots \text{ and } \mathcal{I} \models F_n$，

因此，$\mathcal{I} \models q_1 \wedge \dots \wedge q_m$，根据 $\mathcal{I}$ 的定义：

$$F_1,\dots,F_n \vdash q_1 \text{ and } \dots \text{ and } F_1, \dots, F_n \vdash q_m$$

合并结果，我们得到：

$$F_1, \dots, F_n \vdash q_1, \dots, q_m$$

综上所述，完备性得证。

### 问题 3

- **仿照教材上的方式，为逻辑程序定义一个结构作为它的解释。**
- **若一个逻辑程序P是一致的，那么它就拥有一个模型（因为它只包含闭公式）。仿照极大一致集的方式，在你定义的结构中构造出P的模型。（提示：Herbrand Model）**

【解析】

定义逻辑程序的解释结构需要明确解释逻辑程序中的各个成分，以及如何通过这些成分来解释逻辑程序的语义。以下是一个常见的方式：

1. **逻辑语言**

逻辑程序使用的语言通常包括:
- 符号：常量符号（表示对象），函数符号（表示函数），谓词符号（表示关系）。
- 变量：用来表示任意对象。
- 项：由常量、变量和函数符号构成。
- 原子公式：由谓词符号和项构成，如 $P(x, y)$ 。
2. **语法**

逻辑程序的语法定义了如何构造合法的表达式。常见的构造包括:
- 谓词逻辑公式：基本单元是原子公式，复杂公式通过逻辑连接词（如 $\wedge 、 \vee 、 \neg 、 \rightarrow ）$ 和量词 （如 $\forall 、 \exists ）$ 构造。
- 规则：形如 $H \leftarrow B_1, B_2, \ldots, B_n$ 的结构，其中 $H$ 是头部（结论）， $B_i$ 是体部（条件）。
3. **语义**

逻辑程序的语义通过解释结构 (Interpretation) 来定义。解释结构包括:

- 域 (Domain)：符号解释的基础集合。

- 解释函数 (Interpretation Function)：为语言中的每个符号赋予具体含义。具体包括:

  常量解释：每个常量符号对应域中的一个对象。

  函数解释：每个函数符号对应一个从域到域的映射。

  谓词解释：每个谓词符号对应域上的一个关系。

构造逻辑程序 $P$ 的模型可以通过 Herbrand Model 的方法进行。Herbrand Model 是一种特殊的模型，在这种模型中，所有常量、函数和谓词都仅通过它们在逻辑程序中的定义来解释。下面是具体的构造步骤：

1. 构造 Herbrand 基：列出程序 $P$ 中的所有常量、函数符号和谓词符号，构造所有可能的项和原子公式。
2. 构造极大一致集：从程序 $P$ 中的所有事实（没有条件的逻辑规则）开始，对每个规则 $H \leftarrow B_1, B_2, \ldots, B_n$ 如果 $B_1, B_2, \ldots, B_n$ 在当前一致集内为真，那么将 $H$ 添加到一致集中。重复直到没有新的公式可以添加，将生成的所有一致子句集合扩展成一个极大一致集。

3. 定义 Herbrand 模型 $\mathcal{M}=\{$ 原子公式 $\mid$ 原子公式在极大一致集 $M$ 中为真 $\}$ 。