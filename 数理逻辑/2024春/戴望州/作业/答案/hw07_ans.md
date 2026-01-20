## 第七次作业
### 1 证明 ( 二选一)
#### 1. [Enderton, pp.145] (语义 EI 规则) 假设常数符 $c$ 在 wff $\varphi$ 和 $\psi$ 以及 wff 集 $\Gamma$ 中从未出现, 且 $\Gamma \cup\left\{\varphi_c^x\right\} \vDash \psi$,证明（不使用可靠性与完备性定理） $\Gamma \cup\{\exists x \varphi\} \vDash \psi$​.

$\Gamma ; \varphi_c^x \models \psi$ 
$\Leftrightarrow$ 对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\models_{\mathfrak{A}} \varphi_c^x[s]$，则 $\models_{\mathfrak{A}} \psi[s]$ 
$\Leftrightarrow$  对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \psi[s]$，则 $\nvDash_{\mathfrak{A}} \varphi_c^x[s]$ 
$\Leftrightarrow$ 对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \psi[s]$，则 $\models_{\mathfrak{A}} \neg \varphi_c^x[s]$ 
$\Leftrightarrow$  对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \psi[s]$，则 $\models_{\mathfrak{A}} \neg \varphi\left[s\left(x \mid c^{\mathfrak{A}}\right)\right]$ 
$\Leftrightarrow$  (由于 $c$ 不出现在 $\Gamma, \psi$ 或 $\varphi$ 中，因此 $\Rightarrow$) 对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \psi[s]$，则对于所有 $d \in|\mathfrak{A}|$，$\models_{\mathfrak{A}} \neg \varphi[s(x \mid d)]$ 
$\Leftrightarrow$ 对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \psi[s]$，则 $\models_{\mathfrak{A}} \forall x \neg \varphi[s]$ 
$\Leftrightarrow$ 对于任意 $\mathfrak{A}$ 和 $s$，如果 $\models_{\mathfrak{A}} \Gamma[s]$ 并且 $\nvDash_{\mathfrak{A}} \forall x \neg \varphi[s]$，则 $\models_{\mathfrak{A}} \psi[s]$ 
$\Leftrightarrow$ $\Gamma ; \neg \forall x \neg \varphi \models \psi$

#### 2. [Enderton, pp.I45] 假设 $\Gamma \vdash \varphi$, 且 $P$ 是一个从未出现在 $\Gamma$ 和 $\varphi$ 中的谓词符号。问: 是否存在一个从 $\Gamma$ 出发到 $\varphi$ 的证明, 其中 $P$ 不出现?

##### 定性证明：
$\Gamma \vdash \varphi$ 意味着 $\Gamma \models \varphi$。

对于没有 $P$ 的语言中的每个结构 $\mathfrak{A}$ 和 $s: V \rightarrow|\mathfrak{A}|$ ：
如果 $\models_\mathfrak{A} \Gamma[s]$，则考虑扩展 $\mathfrak{A}$ 并定义 $P^{\mathfrak{A}}=\emptyset$ 的相应结构 $\mathfrak{A}^{\prime}$。
有 $\models_{\mathfrak{A}^{\prime}} \Gamma[s]$（因为 $\Gamma$ 中没有使用 $P$ 的命题），因此，$\models_{\mathfrak{A}^{\prime}} \varphi[s]$，意味着 $\models_{\mathfrak{A}} \varphi\left[s^{\prime}\right]$。

因此，没有 $P$ 的语言中的 $\Gamma \models \varphi$ 成立，且 $\Gamma \vdash \varphi$。

##### 语法上严格证明：
*很麻烦，因为要替换谓词，这个不属于以前定义过的常规操作，可以只看上面的定性证明*
$\Gamma \vdash \varphi$ 意味着存在一个可能使用 $P$ 的从 $\Gamma$ 推导出 $\varphi$ 的推导。我们证明该推导可以更改为不包含 $P$ 的推导。在推导中的每个 $P t_1 \ldots t_n$ 都是一个原子子公式，它是一个合取规则的一部分或一个有效的逻辑公理，因此我们可以希望通过推导将其更改为另一个原子公式，并保持推理的有效性。将推导中每个公式 $\psi$ 中的每个 $P t_1 \ldots t_n$ 更改为 $Q u_1 \ldots u_m$ 的操作写为 $\psi_Q^P$，我们需要这种替换需要确保哪些性质。首先，我们考虑逻辑公理。

1. $\psi$ 是一个重言式。那么，通过在所有地方用另一个原子公式替换一个原子公式，$\psi_Q^P$ 仍然是一个重言式。
2. $\psi$ 是 $\forall x \alpha \rightarrow \alpha_t^x$，其中 $t$ 可以替换为 $\alpha$ 中的 $x$。$\psi_Q^P$ 是 $\forall x \alpha_Q^P \rightarrow\left(\alpha_Q^P\right)_t^x$，其中 $t$ 必须可以替换为 $\alpha_Q^P$ 中的 $x$。唯一的情况是 $t$ 不可以替换为 $\alpha_Q^P$ 中的 $x$，这是因为有一个子公式 $\forall y \beta_Q^P$ 使得 $y \neq x，x$ 在 $\beta_Q^P$ 中是自由的，并且 $y$ 出现在 $t$ 中。如果 $t$（包含 $y$）可以替换 $\forall y \beta$，则 $x$ 在 $\beta$ 中不是自由的。因此，为了确保我们的替换不会产生替换问题，我们只需要确保 $Q u_1 \ldots u_m$ 不包含任何新的（自由）变量，这些变量在任何地方都作为替换的主体。例如，我们可以使用与 $P$ 相同的术语（如果我们有另一个 $n$ 元谓词 $Q$），或使用在推导中根本不出现的变量。
3. $\forall x(\alpha \rightarrow \beta) \rightarrow(\forall x \alpha \rightarrow \forall x \beta)$ 变为 $\forall x\left(\alpha_Q^P \rightarrow \beta_Q^P\right) \rightarrow\left(\forall x \alpha_Q^P \rightarrow \forall x \beta_Q^P\right)$。
4. 如果 $\psi$ 是 $\alpha \rightarrow \forall x \alpha$，其中 $x$ 在 $\alpha$ 中不是自由的，则 $\psi_Q^P$ 变为 $\alpha_Q^P \rightarrow \forall x \alpha_Q^P$，其中 $x$ 在 $\alpha_Q^P$ 中不是自由的，如果 $Q u_1 \ldots u_m$ 不包含作为量化变量（quantified variable）出现的新（自由）变量。
5. $x=x$ 保持不变。
6. $x=y \rightarrow \alpha \rightarrow \alpha^{\prime}$ 保持不变，如果 $\alpha \neq P t_1 \ldots t_n$；否则变为 $x=y \rightarrow Q u_1 \ldots u_m \rightarrow\left(Q u_1 \ldots u_m\right)^{\prime}$，我们需要定义 $\left(Q u_1 \ldots u_m\right)^{\prime}$ 的含义。下文会进行阐述。

接下来，如果 $\psi$ 是通过合取得到的，那么它一定是从某个 $\delta$ 和 $\delta \rightarrow \psi$ 导出的，它们变成 $\delta_Q^P$ 和 $\delta_Q^P \rightarrow \psi_Q^P$，分别表示通过合取得到 $\psi_Q^P$，只要 $\delta_Q^P \rightarrow \psi_Q^P$ 与 $(\delta \rightarrow \psi)_Q^P$ 相同。 总体而言，我们需要确保替换的以下性质：在 $P t_1 \ldots t_n$ 替换为 $Q u_1 \ldots u_m$ 的替换中，我们需要 $Q u_1 \ldots u_m$ 不引入任何新的（相对于 $P t_1 \ldots t_n$）自由变量 $x$，这些变量出现在 $\alpha_t^x$ 或 $\forall x$ 中，并且替换 $(\alpha \rightarrow \beta)_Q^P$ 始终与 $\left(\alpha_Q^P \rightarrow \beta_Q^P\right)$ 以相同的方式进行，对于 $\neg$ 和 $\forall$ 也是如此。这涉及所有公理。我们可以看到唯一可能有问题的公理组是公理组 6，我们需要确保 $\left(\left(P t_1 \ldots t_n\right)^{\prime}\right)_Q^P$ 始终等于 $\left(Q u_1 \ldots u_m\right)^{\prime}$，即如果 $P t_1^{\prime} \ldots t_n^{\prime}$ 是通过在某些地方用 $y$ 替换 $x$ 从 $P t_1 \ldots t_n$ 得到的，那么 $\left(P t_1^{\prime} \ldots t_n^{\prime}\right)_Q^P$ 也是通过从 $\left(P t_1 \ldots t_n\right)_Q^P$ 出发在某些地方用 $y$ 替换 $x$得到的。

事实上，如果语言中有等号，我们可以做一些简单的事情，比如将所有 $P t_1 \ldots t_n$ 替换为 $z=z$，而不管项是什么，其中 $z$ 是在推导中的任何公式中都不出现的变量。更进一步讲，$z=z$ 不引入任何新的自由变量，并且公理组 6 的任何非素数公式变为 $x=y \rightarrow z=z \rightarrow z=z$ 是可以的。如果语言中没有等号，那么我们可以使用任何其他谓词符号 $Q$ 并将 $Q z \ldots z$ 替换为 $P t_1 \ldots t_n$（必须至少有一个与 $P$ 不同的 $Q$，否则不会有任何不包含 $P$ 的原子公式。

### 证明 (二选一)
#### 1. [Enderton, pp.146] 令 $\Gamma=\left\{\neg \forall v_1 P v_1, P v_2, P v_3, \ldots\right\}$. 请问 $\Gamma$​ 是一致的吗? 它是可满足的吗? 请证明你的结论。

根据完备性和正确性定理，两个问题的答案应该是相同的。很容易看出 $\Gamma$ 是可满足的。考虑 $\mathfrak{A}=({0,1} ; P)$，其中 $P^{\mathfrak{A}}={<1>}$ 且 $s: V \rightarrow|\mathfrak{A}|$，使得 $s\left(v_i\right)=1$。那么，显然 $\models_{\mathfrak{A}} P v_i[s]$，$\models_{\mathfrak{A}} P v_1\left[s\left(v_1 \mid 1\right)\right]$ 并且 $\nvdash_{\mathfrak{A}} P v_1\left[s\left(v_1 \mid 0\right)\right]$，因此，$\nvdash_{\mathfrak{A}} \forall v_1 P v_1[s]$。

注意，有些人可能会认为 $\Gamma$ 既不一致也不可满足。确实，第一个公式表示 $P$ 对域中的每个元素都不成立，然后它列出了所有可能的变量，说 $P$ 对它们都成立。这个方法的问题在于，第一个公式确实说域中有一个元素 $P$ 不成立。然而，在此之后，$\Gamma$ 并没有列出域中的所有元素，而是包含了一个无限的独立变量列表，说无论分配给每个变量的元素是什么，$P$ 对该元素成立。换句话说，$\Gamma$ 的其余部分只是说有一个元素 $P$ 成立。换句话说，$\Gamma$ 在某种程度上（并非真正逻辑上）等价于 $\Gamma^{\prime}={\exists x \neg P x, \exists y P y}$，意思是对于每个可以满足 $\Gamma$ 的域及某个 $s$，$\Gamma^{\prime}$（仅包含句子的）是满足的，反之亦然。

#### 2. [Enderton, pp.I46] 证明：一张无穷的地图（有无穷个国家）能用四种颜色着色, 当且仅当它的每一个有穷的子地图可以。

引入句子符号 $A_{i, j}$，其中 $v\left(A_{i, j}\right)=T$ 意味着国家 $i$ 被染色为颜色 $j$，并形成两组句子，一组由 $B_i$ 组成，当且仅当 $v\left(A_{i, j}\right)$ 中的一个（且仅一个）$j \in{1,2,3,4}$ 为真时，$\bar{v}\left(B_i\right)=T$（每个国家恰好被染色一种颜色）；另一组由 $D_{i, j, k}$ 组成，对于这样的一组 $i$ 和 $k$，即国家 $i$ 和 $j$ 相邻，当且仅当 $v\left(A_{i, j}\right)$ 和 $v\left(A_{k, j}\right)$ 中至多一个为真时，$\bar{v}\left(D_{i, j, k}\right)=T$（相邻国家不能染成相同的颜色）。然后我们会使用命题逻辑的紧致性定理来论证，只要句子 $B_i$ 和 $D_{i, j, k}$ 的任何有限子集 $\Sigma$ 是可满足的，整个 $\Sigma$ 也是可满足的。

以上，我们构造一个一阶语言和一组句子 $\Gamma$ 来描述地图的着色，并应用紧致性定理。我们将使用一个原子公式 $\alpha_{i, j}$，等同于 $P_j c_i$，而不是句子符号 $A_{i, j}$，以确保所有这样的原子公式是不同的。然后我们从 $\alpha_{i, j}$ 构造句子 $\beta_i\left(B_i\right)$ 和 $\delta_{i, j, k}\left(D_{i, j, k}\right)$，并定义 $\Gamma=\{\beta_i, \delta_{i, j, k}\}_{i, j, k}$。这里，$|\mathfrak{A}|$ 可以被认为是一组代表所有国家的点，然后 $c_i^{\mathfrak{A}}$ 是 $|\mathfrak{A}|$ 中代表国家 $i$ 的一个点，$P_j^{\mathfrak{A}}$ 是 $|\mathfrak{A}|$ 中被染色为颜色 $j$ 的点的子集。句子 $\beta_i$ 确保了恰好有一个 $P_j^{\mathfrak{A}}$ 关系对 $c_i^{\mathfrak{A}}$ 成立（对应国家 $i$ 的点被染成恰好一种颜色），而 $\delta_{i, j, k}$ 确保了 $P_j^{\mathfrak{A}}$ 关系不对 $c_i^{\mathfrak{a}}$ 和 $c_k^{\mathfrak{d}}$ 都成立（对应相邻国家 $i$ 和 $k$ 的点中至少有一个没有染成颜色 $j$）。现在，当且仅当{当且仅当国家 $i$ 被染成颜色 $j$，$\Gamma$ 的模型 $\mathfrak{A}$ 才是正确的}时，$\mathfrak{A}$ 是 $\Gamma$ 的模型。而根据紧致性定理的推论，当且仅当 $\Gamma$ 的每个有限子集有一个模型时，$\Gamma$ 才有一个模型。因此，如果无限图的正确着色存在，那么 $\Gamma$ 有一个模型，它的每个有限子集都有一个模型。反之亦然，如果每个有限子图都有一个正确的着色，那么类似于命题逻辑，给定 $\Gamma$ 的有限子集 $\Gamma_0$，首先，将其扩展为包含所有 $\Gamma_0$ 中的句子和对应某些有限子图的正确着色的所有句子的有限子集 $\Gamma^{\prime}$，然后论证 $\Gamma^{\prime}$（因此 $\Gamma_0$）的模型存在，因此，根据紧致性定理，$\Gamma$ 的模型存在，无限图有一个正确的着色。

现在，与建议的不同，一个更有趣的问题是，是否可以通过利用一阶语言的全部功能，使用有限语言获得类似的结果。在这里，我们可以使用无限变量而不是常量来分配颜色。因此，假设 $|\mathfrak{A}|$ 是四色的集合（一个句子 $\forall v_1 \ldots \forall v_5 v_1=v_2 \vee v_1=v_3 \vee \ldots \vee v_4=v_5$）。然后，分配 $s: V \rightarrow|\mathfrak{A}|$ 表示国家的着色，通过定义确保每个国家被染成一种颜色，因为 $s$ 是一个函数（所以我们根本不需要 $B_i$ 的类似物）。进一步，对于每对相邻国家 $i$ 和 $k$，我们简单地添加一个谓词公式，表示 $\neg v_i=v_k$。这个谓词公式确保两个相邻国家被分配不同的颜色。就是这样！结构 $\mathfrak{A}$ 满足 $\Gamma$ 和 $s$ 当且仅当 $|\mathscr{Q}|$ 包含不超过4个点（颜色），并且每个变量 $v_i$（国家 $i$）由 $s$ 分配到 $|\mathfrak{A}|$ 的一个点（颜色），使得没有两个相邻国家共享相同的颜色。然后我们可以以相同的方式应用紧致性定理，声明当且仅当 $\Gamma$ 的每个有限子集是可满足的，$\Gamma$ 才是可满足的。

### 3 证明 (四选二)
[Enderton, pp.I46] 完备性定理告诉我们, 每个语句要么是有效的, 即存在一个证明 (从 $\emptyset$ 出发); 要么就有一个结构令其为假。请判断下面的语句是否有效, 并证明你的结论
#### (a) $\forall x(Q x \rightarrow \forall y Q y)$

该句子无效。

设 $\mathfrak{A}=({0,1} ; Q)$，其中 $Q^{\mathfrak{A}}={<1>}$。
那么，对于任何 $s: V \rightarrow|\mathfrak{A}|$，$\nvdash_{\mathfrak{A}} Q x[s(x \mid 0)]$ 并且 $\models_{\mathfrak{A}} Q x[s(x \mid 1)]$
因此，$\nvdash_{\mathfrak{A}} \forall y Q y[s]$，$\nvdash_{\mathfrak{A}} Q x \rightarrow \forall y Q y[s(x \mid 1)]$，并且 $\nvdash_{\mathfrak{A}} \forall x(Q x \rightarrow \forall y Q y)[s]$。

#### (b) $(\exists x P x \rightarrow \forall y Q y) \rightarrow \forall z(P z \rightarrow Q z)$

该句子有效。

我们需要证明 $\vdash(\exists x P x \rightarrow \forall y Q y) \rightarrow \forall z(P z \rightarrow Q z)$。
根据推导和泛化定理，只需证明 $\exists x P x \rightarrow \forall y Q y ; P z \vdash Q z$。
根据公理组2，MP和反证法，只需证明 $P z ; \neg \forall y Q y \vdash \neg(\exists x P x \rightarrow \forall y Q y)$。
根据MP和反证法，使用公理组2的 $\vdash \forall x \neg P x \rightarrow \neg P z$，我们有 $P z \vdash \exists x P x$。
使用公理组1的 $\vdash \exists x P x \rightarrow \neg \forall y Q y \rightarrow \neg(\exists x P x \rightarrow \forall y Q y)$ 和MP，我们有 $P z ; \neg \forall y Q y \vdash \neg(\exists x P x \rightarrow \forall y Q y)$。

#### (c) $\forall z(P z \rightarrow Q z) \rightarrow(\exists x P x \rightarrow \forall y Q y)$

该句子无效。

一个使其无效的结构的例子与(a)中相同，其中 $P^{\mathfrak{A}}=Q^{\mathfrak{A}}$。
对于任何 $s: V \rightarrow|\mathfrak{A}|$，$\models_{\mathfrak{A}} P z \rightarrow Q z[s]$，$\models_{\mathfrak{A}} \neg P x[s(x \mid 0)]$，$\nvdash_{\mathfrak{A}} \neg P x[s(x \mid 1)]$，$\nvdash_{\mathfrak{A}} Q x[s(x \mid 0)]$ 并且 $\models_{\mathfrak{A}} Q x[s(x \mid 1)]$

因此，$\models_{\mathfrak{A}} \forall z(P z \rightarrow Q z)[s]$，$\nvdash_{\mathfrak{A}} \forall x \neg P x[s]$，$\models_{\mathfrak{A}} \exists x P x[s]$，$\nvdash_{\mathfrak{A}} \forall y Q y[s]$，$\nvdash_{\mathfrak{A}} \exists x P x \rightarrow \forall y Q y[s]$，并且 $\nvdash_{\mathfrak{A}} \forall z(P z \rightarrow Q z) \rightarrow(\exists x P x \rightarrow \forall y Q y)[s]$。

#### (d) $\neg \exists y \forall x(P x y \leftrightarrow \neg P x x)$

该句子有效。

我们需要证明 $\vdash \neg \exists y \forall x(P x y \leftrightarrow \neg P x x)$
等价于$\vdash \forall y \neg \forall x \neg((P x y \rightarrow \neg P x x) \rightarrow \neg(\neg P x x \rightarrow P x y))$（这里我们使用 $\leftrightarrow$：$\alpha \leftrightarrow \beta$ 意味着 $\neg((\alpha \rightarrow \beta) \rightarrow \neg(\beta \rightarrow \alpha))$）。

根据泛化定理，只需证明 $\vdash \neg \forall x \neg((P x y \rightarrow \neg P x x) \rightarrow \neg(\neg P x x \rightarrow P x y))$，我们记为 $\vdash \neg \forall x \neg \gamma$。

为此，只需证明 $\vdash \gamma_t^x$，其中 $t$ 是 $\gamma$ 中可以替换 $x$ 的一个项。

根据公理组2，$\vdash \forall x \neg \gamma \rightarrow \neg \gamma_t^x$，并且使用MP和反证法，我们有 $\gamma_t^x \vdash \neg \forall x \neg \gamma$。现在，$y$ 可以替换 $\gamma$ 中的 $x$，并且 $\gamma_y^x$ 只是 $(P y y \rightarrow \neg P y y) \rightarrow \neg(\neg P y y \rightarrow P y y)$，这是一个重言式。​