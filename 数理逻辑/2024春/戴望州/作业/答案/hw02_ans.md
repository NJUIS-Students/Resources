---
南京大学（苏州校区） 数理逻辑（2024春）任课教师：戴望州 课程主页： https://daiwz.net/teaching/
---

# 作业 - 02（参考答案）

题目：设 $\Gamma$ 是一个命题 *wff* 集合，$\alpha$ 与 $\beta$ 为 *wff*，试证明以下命题：
### 1. $\alpha$ 是重言式，当且仅当 $\emptyset \vDash \alpha$ 
- 证明必要性： $\alpha$ 为重言式，则每个真值指派均满足 $\alpha$，即 $\Sigma \vDash \alpha$ 中对任意 $\Sigma$ 的真值指派均满足$\alpha$。令 $\Sigma$ 为 $\emptyset$，则得到 $\emptyset \vDash \alpha$；
- 证明充分性：因为 $\emptyset \vDash \alpha$，所以满足 $\emptyset$ 的真值指派也满足$\alpha$，而任意真值指派均满足 $\emptyset$ 中的元素，则任意真值指派也均满足$\alpha$，所以 $\alpha$ 是重言式。

### 2. 若 $\Gamma \vDash \alpha$，且 $\Gamma \vDash \alpha \rightarrow \beta$，则 $\Gamma \vDash \beta$
由 $\Gamma \vDash \alpha$，以及 $\Gamma \vDash \alpha \rightarrow \beta$，可得：对于任意满足 $\Gamma$ 的真值指派 $v$，均满足 $\alpha$ 和 $\alpha \rightarrow \beta$，即 $v(\alpha)=T$，$v(\alpha \rightarrow \beta)=T$。

由真值表可知：当 $v(\alpha)=T$ 与 $v(\alpha \rightarrow \beta)=T$ 时，有 $v(\beta)=T$。即对于任意满足 $\Gamma$ 的真值指派 $v$，均满足 $\beta$，为 $\Gamma \vDash \beta$。

| $\alpha$ | $\beta$ | $(\alpha \rightarrow \beta)$ |
| :------: | :-----: | :--------------------------: |
|    T     |    T    |              T               |
|    T     |    F    |              F               |
|    F     |    T    |              T               |
|    F     |    F    |              T               |

### 3. **紧致性 **(Compactness): 若 $\Gamma$ 是可满足的，那么 $\Gamma$ 的任意有穷子集均是可满足的
$\Gamma$ 是可满足的，即存在一种真值指派 $v$ 使得 $v \vDash \Gamma$，令命题公式集合 $\Gamma = \{ \alpha_{1},\alpha_{2},\cdots ,\alpha_{n} \}$，则对任意 $\alpha_{i}\in \Gamma$，有 $v \vDash \alpha_{i}$。

反证法：假设存在一个 $\Gamma$ 的有穷子集 $\Gamma_{0} \subseteq \Gamma$，对于上述真值指派 $v$，使得$v \nvDash \Gamma_{0}$。即存在至少 1 个 $\alpha_{k}\in \Gamma_{0}$ 使得 $v \nvDash \alpha_{k}$。因为 $\alpha_{k} \in \Gamma$，则对于命题公式集合 $\Gamma = \{ \alpha_{1},\alpha_{2},\cdots ,\alpha_{n} \}$，$\exists \alpha_{k} \in \Gamma$ 使得 $v \nvDash \alpha_{k}$，与 “$\Gamma$ 是可满足的” 矛盾。因此若 $\Gamma$ 是可满足的，那么 $\Gamma$ 的任意有穷子集均是可满足的。

### 4. **单调性** (Monoticity): 若 $\Gamma \subseteq \Delta$ 且 $\Gamma \vDash \alpha$, 那么同样有 $\Delta \vDash \alpha$

根据定义，要证 $\Delta \vDash \alpha$，只要证所有满足 $\Delta$ 的真值指派均满足 $\alpha$。

- 若不存在真值指派能满足 $\Delta$，且 $\Gamma \subseteq \Delta$，也不存在真值指派能满足 $\Gamma$，显然有 $\Delta \vDash \alpha$；
- 若存在真值指派 $v$ 能满足 $\Delta$，即 $v\vDash \Delta$，此时有对任意 $\alpha_i \in \Delta$，有 $v\vDash \alpha_i$，因此有 $v\vDash \Gamma$，又因为 $\Gamma \vDash \alpha$, 则 $v\vDash  \alpha$，换言之，满足 $\Delta$ 的真值指派都能满足 $\alpha$，得证 $\Delta \vDash \alpha$ 。

### 5. **传递性** (Transitivity): 若 $\Gamma \models \alpha$ 且 $\Delta \cup \{\alpha\} \models \beta$，那么有 $\Gamma \cup \Delta \models \beta$

由 $\Gamma \models \alpha$ 和定义1.14 知，对于任意的真值指派 $v$，如果 $v \models \Gamma$，那么 $v \models \alpha$；由 $\Delta \cup \{\alpha\} \models \beta$ 和定义1.14知，对于任意的真值指派 $v'$，如果 $v' \models \Delta$ 且 $v' \models \alpha$，那么 $v' \models \beta$。

由 $v$ 和 $v'$ 的任意性，取 $v'$ 为满足前一个条件的真值指派 $v$，则有：对于任意的真值指派 $v$，如果$v \models \Gamma$且$v \models \Delta$，那么$v \models \beta$，即：对于任意的真值指派$v$，如果$v \models \Gamma \cup \Delta$，那么$v \models \beta$，即：$\Gamma \cup \Delta \models \beta$，证毕。