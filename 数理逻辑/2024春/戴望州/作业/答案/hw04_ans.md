## 第四次作业
### 证明 \[Enderton,pp.130,10] $\forall x \forall y Pxy \vdash \forall y \forall x Pyx$

$$
\begin{eqnarray*}
	1. \quad && \forall x \forall y Pxy \vdash \forall x \forall z Pxz & \quad \text{Ax}\,2.7.2, \text{Generalization}\\
	2. \quad && \vdash \forall x \forall z Pxz \rightarrow \forall z Pyz & \quad \text{Deduction, Ax}\,2.7.2 \\
	3. \quad &&\vdash \forall z Pyz \rightarrow Pyx & \quad \text{Ax}\,2.7.2 \\
	4. \quad && \forall x \forall y Pxy \vdash Pyx & \quad \text{Deduction, 三段论} \\
	5. \quad && \forall x \forall y Pxy \vdash \forall y \forall x Pyx & \quad \text{Generalization}\\
\quad \tag*{Q.E.D}
\end{eqnarray*}
$$

### 2 证明 \[Enderton, pp.131, 15-17]
#### 2.1 第一组

##### 1.$~\vdash \exists x \alpha \vee \exists x \beta \leftrightarrow \exists x(\alpha \vee \beta)$

证明：

我们需要证明 $\vdash(\neg \exists x \alpha \rightarrow \exists x \beta) \rightarrow \exists x(\neg \alpha \rightarrow \beta)$ 和 $\vdash \exists x(\neg \alpha \rightarrow \beta) \rightarrow \neg \exists x \alpha \rightarrow \exists x \beta$ 。通过演绎和逆否命题，我们只需证明：

-  $\forall x \neg(\neg \alpha \rightarrow \beta) \vdash \neg(\forall x \neg \alpha \rightarrow \neg \forall x \neg \beta)$ 
- $\neg(\forall x \neg \alpha \rightarrow \neg \forall x \neg \beta) \vdash \forall x \neg(\neg \alpha \rightarrow \beta)$ 

对于第一个命题， 对 $\gamma, \delta \models \neg(\gamma \rightarrow \neg \delta)$ 使用规则 T，我们只需证明 $\forall x \neg(\neg \alpha \rightarrow \beta) \vdash \forall x \neg \alpha$ 和 $\forall x \neg(\neg \alpha \rightarrow \beta) \vdash \forall x \neg \beta$。通过 MP 规则，我们只需证明 $\vdash \forall x \neg(\neg \alpha \rightarrow \beta) \rightarrow \forall x \neg \alpha$ 和 $\vdash \forall x \neg(\neg \alpha \rightarrow \beta) \rightarrow \forall x \neg \beta$ ，然后通过 MP 规则和概括定理，我们只需证明 $\vdash \neg(\neg \alpha \rightarrow \beta) \rightarrow \neg \alpha$ 和 $\vdash \neg(\neg \alpha \rightarrow \beta) \rightarrow \neg \beta$ 。显然，这两个都是重言式，得证原命题。

对于第二个命题，通过概括定理和逆否命题，我们只需证明 $\neg \alpha \rightarrow \beta \vdash \forall x \neg \alpha \rightarrow \neg \forall x \neg \beta$ 。通过演绎定理，我们只需证明 $\forall x \neg \alpha ; \neg \alpha \rightarrow \beta \vdash \neg \forall x \neg \beta$ 。通过 RAA（归谬），我们只需证明出 $\{\forall x \neg \alpha, \neg \alpha \rightarrow \beta, \forall x \neg \beta\}$ 是不一致的。通过 $\vdash\forall x \neg \alpha \rightarrow \neg \alpha$ 和 $\vdash \forall x \neg \beta \rightarrow \neg \beta$ 以及 MP 规则，得到 $\{\forall x \neg \alpha, \neg \alpha \rightarrow \beta, \forall x \neg \beta\} \vdash\{\beta, \neg \beta\}$ 。因此， $\{\forall x \neg \alpha, \neg \alpha \rightarrow \beta, \forall x \neg \beta\}$ 是不一致的，得证原命题。

##### 2.$~\vdash \forall x \alpha \vee \forall x \beta \rightarrow \forall x(\alpha \vee \beta)$

证明：

同理，通过演绎定理、概括定理和逆否命题，我们只需证明 $\neg(\neg \alpha \rightarrow \beta) \vdash$ $\neg(\neg \forall x \alpha \rightarrow \forall x \beta)$ 。为此，对 $\gamma, \neg\delta \models \neg(\gamma \rightarrow  \delta)$ 使用规则 T，我们只需证明 $\neg(\neg \alpha \rightarrow \beta) \vdash \neg \forall x \alpha$ 和 $\neg(\neg \alpha \rightarrow \beta) \vdash \neg \forall x \beta$，换言之只需证明 $\{\neg(\neg \alpha \rightarrow \beta), \forall x \alpha\}$ 和 $\{\neg(\neg \alpha \rightarrow \beta), \forall x \beta\}$ 都是不一致的。

由于 $\vdash \forall x \alpha \rightarrow \alpha$ 和 $\vdash \forall x \beta \rightarrow$ $\beta$，以及 $\neg(\neg \alpha \rightarrow \beta) \rightarrow \neg \alpha$ 和 $\neg(\neg \alpha \rightarrow \beta) \rightarrow \neg \beta$ 都是重言式，通过规则 T 得到 $\{\neg(\neg \alpha \rightarrow \beta), \forall x \alpha\} \vdash\{\alpha, \neg \alpha\}$ 和 $\{\neg(\neg \alpha \rightarrow \beta), \forall x \beta\} \vdash\{\beta, \neg \beta\}$ ，因此不一致，得证原命题。

#### 2.2 第二组

##### 1. $\exists x (\alpha \wedge \beta) \rightarrow \exists x \alpha \wedge \exists x \beta$.

证明：

我们需要证明 $\vdash \exists x \neg(\alpha \rightarrow \neg\beta) \rightarrow \neg(\exists x \alpha \rightarrow \neg \exists x \beta)$ .依次使用演绎定理、逆否命题等价、概括定理以及再次使用逆否命题等价，我们只需证 $\neg(\alpha \rightarrow \neg\beta) \vdash \neg(\neg \forall \neg \alpha \rightarrow \forall x \neg \beta)$ .为了证明它，我们只需证 $\neg(\alpha \rightarrow \neg \beta) \vdash \neg \forall x \neg \alpha$ 和 $\neg(\alpha \rightarrow \neg \beta) \vdash \neg \forall x \neg \beta$ (通过对 $\gamma, \neg \delta \models \neg(\gamma \rightarrow \delta)$ 使用T规则得到)，或者 $\{\neg(\alpha \rightarrow \neg \beta), \forall x \neg \alpha\}$ 和 $\{\neg(\alpha \rightarrow \neg \beta), \forall x \neg \beta\}$ 都是不一致的. 根据Ax 2.7.2可得 $\vdash \forall x \neg \alpha \rightarrow \neg \alpha$ 和 $\vdash \forall x \neg \beta \rightarrow \neg \beta$ 并且有 $\neg(\alpha \rightarrow \neg \beta) \rightarrow \alpha$ 和 $\neg(\alpha \rightarrow \neg \beta) \rightarrow \beta$ 是重言式. 所以根据T规则，$\{\neg(\alpha \rightarrow \neg \beta), \forall x \neg \alpha\} \vdash \{\alpha, \neg\alpha\}$ 且 $\{\neg(\alpha \rightarrow \neg \beta), \forall x \neg \beta\} \vdash \{\beta, \neg \beta\}$. 原命题得证.

##### 2. $\forall x (\alpha \wedge \beta ) \leftrightarrow \forall x \alpha \wedge \forall x \beta$

证明：

我们需要证明$\vdash \forall x \neg(\alpha \rightarrow \neg \beta) \rightarrow \neg (\forall x \alpha \rightarrow \neg \forall x \beta)$ 和 $\vdash \neg(\forall x \alpha \rightarrow \neg \forall x \beta) \rightarrow \forall x \neg(\alpha \rightarrow \neg \beta)$. 根据演绎定理，我们只需证明：

- $\forall x \neg(\alpha \rightarrow \neg \beta) \vdash \neg (\forall x \alpha \rightarrow \neg \forall x \beta)$
- $\neg(\forall x \alpha \rightarrow \neg \forall x \beta) \vdash \forall x \neg(\alpha \rightarrow \neg \beta)$

对于第一个命题，我们只需证 $\forall x \neg(\alpha \rightarrow \neg \beta) \vdash \forall x \alpha$ 和 $\forall x \neg(\alpha \rightarrow \neg \beta) \vdash \forall x \beta$ （通过对 $\gamma, \delta \models \neg(\gamma \rightarrow \neg \delta)$ 使用T规则得到）. 根据MP规则，只需证$\vdash \forall x \neg(\alpha \rightarrow \neg \beta) \rightarrow \forall x \alpha$ 和 $\forall x \neg(\alpha \rightarrow \neg \beta) \rightarrow \forall x \beta$，根据Ax 2.7.3、MP规则以及概括定理，我们只需证明 $\vdash \neg (\alpha \rightarrow \neg \beta) \rightarrow \alpha$ 和 $\vdash \neg (\alpha \rightarrow \neg \beta)\rightarrow \beta$. 这两个都是重言式，原命题得证.

对于第二个命题，根据概括定理和逆否命题等价，我们只需证 $\alpha \rightarrow \neg \beta \vdash \forall x \alpha \rightarrow \neg \forall x \beta$. 根据演绎定理，只需证明 $\forall x \alpha; \alpha \rightarrow \neg \beta \vdash \neg \forall x \beta$. 根据RAA，我们只需证明 $\{\forall x \alpha, \alpha \rightarrow \neg \beta, \forall x \beta\}$是不一致的. 根据Ax 2.7.2，可得 $\vdash \forall x \alpha \rightarrow \alpha$ 和 $\vdash \forall x \beta \rightarrow \beta$，根据MP规则 $\{\forall x \alpha, \alpha \rightarrow \neg \beta, \forall x \beta\} \vdash \{\beta, \neg \beta\}$. 原命题得证.

#### 2.3 第三组
##### 2.3.1 $\vdash \forall x(\alpha \rightarrow \beta) \rightarrow (\exists x \alpha \rightarrow \exists x \beta)$

证明等价于 $\vdash \forall x(\alpha \rightarrow \beta) \rightarrow \lnot \forall x \lnot \alpha \rightarrow \lnot \forall x \lnot \beta$

$$
\begin{eqnarray*}
	1. \quad && \forall x(\alpha \rightarrow \beta) \vdash \alpha \rightarrow \beta & \quad \text{Deduction, Ax}\,2.7.2 \\ 
	2. \quad && \forall x(\alpha \rightarrow \beta)\vdash \lnot \beta \rightarrow \lnot \alpha & \quad \text{contraposition}\\
	3. \quad && \forall x (\alpha \rightarrow \beta) \vdash  \forall x \lnot \beta \rightarrow \forall x \lnot \alpha & \quad \text{Generalization, Ax 2.7.3} \\
	4. \quad && \{\forall x (\alpha \rightarrow \beta)\} \vdash \lnot \forall x \lnot \alpha \rightarrow \lnot \forall x \lnot \beta  & \quad \text{contraposition}\\
	5. \quad && \{\forall x (\alpha \rightarrow \beta);\lnot \forall x \lnot \alpha\}\vdash \lnot \forall x \lnot \beta  & \quad \text{Deduction}\\
	6. \quad && \vdash \forall x(\alpha \rightarrow \beta) \rightarrow \lnot \forall x \lnot \alpha \rightarrow \lnot \forall x \lnot \beta \quad & \text{Deduction}\\
\quad \tag*{Q.E.D}
\end{eqnarray*}
$$
##### 2.3.2 $\vdash \exists x(Py \land Qx)\leftrightarrow Py \land \exists x\ Q x$ 
因为$\alpha \land \beta$等价于$\lnot(\alpha \rightarrow \lnot \beta)$
所以证明分为两步：

1. 首先证明: $\vdash \lnot \forall x \lnot(\lnot(Py \rightarrow \lnot Qx)) \rightarrow \lnot(Py \rightarrow \forall x \lnot Qx)$
	由Contraposition和Deduction，上式等价于：
	$\{Py \rightarrow \forall x \lnot Qx\} \vdash \forall x \lnot(\lnot(Py \rightarrow \lnot Qx))$
	
	$$
	\begin{eqnarray*}
		1. \quad && Py \rightarrow \forall x \lnot Qx & \quad \text{hypothesis}\\
		2. \quad && \forall x \lnot Qx \rightarrow \lnot Qx & \quad \text{Ax}\,2.7.2\\
		3. \quad && Py \rightarrow \lnot Qx & \quad \text{三段论}\\
		4. \quad && \{Py \rightarrow \forall x \lnot Qx; Py \}\vdash \lnot Qx & \quad \text{monotonicity}\\
		5. \quad && \{Py \rightarrow \forall x \lnot Qx \} \vdash Py \rightarrow \lnot Qx & \quad \text{Deduction} \\
		6. \quad && \{ Py \rightarrow \forall x \lnot Qx \} \vdash \forall x (Py \rightarrow \lnot Qx) & \quad \text{Ax}\,2.7.4 \\
	\end{eqnarray*}
	$$
	易得$\forall x (Py \rightarrow \lnot Qx) \rightarrow \lnot(\lnot(Py \rightarrow \lnot Qx))$
	
	由MP可以得到：$\{Py \rightarrow \forall x \lnot Qx\} \vdash \forall x \lnot(\lnot(Py \rightarrow \lnot Qx))$
	
	得证。
	

2. 然后证明: $\vdash \lnot(Py \rightarrow \forall x \lnot Qx) \rightarrow \lnot \forall x \lnot(\lnot(Py \rightarrow \lnot Qx))$
	
	我们需要从一个重言式出发：$\vdash Py \rightarrow \lnot(\lnot(Py \rightarrow \lnot Qx))\rightarrow \lnot Qx$
	$$
	\begin{eqnarray*}
		1. \quad && Py \vdash \lnot(\lnot(Py \rightarrow \lnot Qx))\rightarrow \lnot Qx & \quad \text{Deduction}\\
		2. \quad && Py \vdash \forall x \lnot(\lnot(Py \rightarrow \lnot Qx))\rightarrow \forall x \lnot Qx & \quad \text{Generalization, Ax 2.7.3} \\
		3. \quad && \forall x \lnot(\lnot(Py \rightarrow \lnot Qx)) \vdash Py \rightarrow \forall x \lnot Qx & \quad \text{Deduction}\\
		4. \quad && \vdash \lnot(Py \rightarrow \forall x \lnot Qx) \rightarrow \lnot \forall x \lnot(\lnot(Py \rightarrow \lnot Qx)) & \quad \text{Contraposition, Deduction}\\
	\quad \tag*{Q.E.D}
	\end{eqnarray*}
	$$