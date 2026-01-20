## 第三次作业
### 1. 证明
#### 1. $\vdash (\alpha \rightarrow \beta)\rightarrow ((\beta \rightarrow \gamma)\rightarrow(\alpha \rightarrow \gamma))$
由演绎定理：
$$
\begin{eqnarray*}
	\quad && \vdash (\alpha \rightarrow \beta)\rightarrow ((\beta \rightarrow \gamma)\rightarrow(\alpha \rightarrow \gamma)) & \quad \\
	\quad && \Leftrightarrow \{ (\alpha \rightarrow \beta) \} \vdash (\beta \rightarrow \gamma)\rightarrow(\alpha \rightarrow \gamma) & \quad \text{Deduction}\\
	\quad && \Leftrightarrow \{ (\alpha \rightarrow \beta);(\beta \rightarrow \gamma) \}\vdash \alpha \rightarrow \gamma & \quad \text{Deduction}\\
	\quad && \Leftrightarrow \{ (\alpha \rightarrow \beta);(\beta \rightarrow \gamma);\alpha \}\vdash \gamma & \quad \text{Deduction}\\
\end{eqnarray*}
$$
即只需证明上式即可
$$
\begin{eqnarray*}
	 1. \quad && \alpha \rightarrow \beta & \quad \text{Hyp} \\
	 2. \quad && \alpha & \quad \text{Hyp} \\
	 3. \quad && \beta & \quad 1,2\,\text{MP}\\
	 4. \quad && \beta \rightarrow \gamma & \quad \text{Hyp} \\
	 5. \quad && \gamma & \quad 4,5\,\text{MP}\\
	 \quad \tag*{Q.E.D}
\end{eqnarray*}
$$
#### 2. Contraposition: 若$\Gamma \cup \{\lnot \alpha \}\vdash \lnot \beta$，则$\Gamma \cup \{\beta \}\vdash \alpha$
由演绎定理，即证：若 $\Gamma \vdash \lnot \alpha \rightarrow \lnot \beta$，则 $\Gamma \vdash \beta \rightarrow \alpha$

首先证明Lemma:  $\vdash (\lnot \alpha \rightarrow \lnot \beta)\rightarrow (\beta \rightarrow \alpha)$
由演绎定理，等价于证明：$\{\lnot \alpha \rightarrow \lnot \beta, \beta\}\vdash \alpha$
$$
\begin{eqnarray*}
	1. \quad && \lnot \alpha \rightarrow \lnot \beta & \quad \text{Hyp}\\
	2. \quad && (\lnot \alpha \rightarrow \lnot \beta)\rightarrow((\lnot \alpha \rightarrow \lnot \lnot \beta)\rightarrow\lnot \lnot \alpha) & \quad \text{Ax}\,1.22.9 \\
	3. \quad &&  (\lnot \alpha \rightarrow \lnot \lnot \beta)\rightarrow\lnot\lnot\alpha & \quad 1,2\,\text{MP}\\
	4. \quad && \lnot \lnot \alpha \rightarrow \alpha & \quad \text{Ax}\,1.22.14 \\
	5. \quad && (\lnot \alpha \rightarrow \lnot \lnot \beta)\rightarrow\alpha & \quad 3,4\,\text{MP}\\
	6. \quad && \lnot \lnot \beta \rightarrow (\lnot \alpha \rightarrow \lnot \lnot \beta) & \quad \text{Ax}\,1.22.7 \\
	7. \quad && \beta \rightarrow \lnot \lnot \beta & \quad \text{Obvious}\\
	8. \quad && \beta \rightarrow (\lnot\alpha \rightarrow \lnot \lnot \beta) & \quad 6,7\,\text{MP}\\
	9. \quad && \beta & \quad \text{Hyp}\\
	10. \quad && \lnot \alpha \rightarrow \lnot \lnot \beta & \quad 8,9\,\text{MP}\\
	11. \quad && \alpha & \quad 5,10\,\text{MP}\\
\quad \tag*{Q.E.D}
\end{eqnarray*}
$$

当$\Gamma \vdash \lnot \alpha \rightarrow \lnot \beta$与Lemma成立时，由MP规则，即证： $\Gamma \vdash \beta \rightarrow \alpha$


#### 3. Double Negation Elimination: $\{\lnot \lnot \alpha\}\vdash \alpha$
$$
\begin{eqnarray*}
	1. \quad && \vdash \lnot \lnot \alpha \rightarrow \alpha & \quad \text{Ax}\,1.22.14 \\
	2. \quad && \{\lnot \lnot \alpha \} \vdash \alpha & \quad \text{Deduction}\\
\quad \tag*{Q.E.D}
\end{eqnarray*}
$$
下面提供一种不使用公理1.22.14的证明
$$
\begin{eqnarray*}
	1. \quad && \lnot \alpha \rightarrow (\alpha \rightarrow \lnot (\lnot \alpha \rightarrow \alpha)) & \quad \text{Ax}\,1.22.10 \\
	2. \quad && (\lnot \alpha \rightarrow (\alpha \rightarrow \lnot (\lnot \alpha \rightarrow \alpha))) \\
	   \quad && \rightarrow ((\lnot \alpha \rightarrow \alpha)\rightarrow(\lnot \alpha \rightarrow \lnot(\lnot \alpha \rightarrow \alpha))) & \quad \text{Ax}\,1.22.8 \\
	3. \quad && (\lnot \alpha \rightarrow \alpha)\rightarrow(\lnot \alpha \rightarrow \lnot(\lnot \alpha \rightarrow \alpha)) & \quad 1,2\,\text{MP} \\
	4. \quad && (\lnot \alpha \rightarrow \lnot(\lnot \alpha \rightarrow \alpha))\rightarrow((\lnot \alpha \rightarrow \alpha)\rightarrow \alpha) & \quad \text{q2. Contraposition}\\
	5. \quad && (\lnot \alpha \rightarrow \alpha)\rightarrow((\lnot \alpha \rightarrow \alpha)\rightarrow \alpha) & \quad 3,4\,\text{三段论} \\
	6. \quad && ((\lnot \alpha \rightarrow \alpha)\rightarrow((\lnot \alpha \rightarrow \alpha)\rightarrow \alpha)) \\
	   \quad && \rightarrow (((\lnot \alpha \rightarrow \alpha)\rightarrow(\lnot \alpha \rightarrow \alpha))\rightarrow((\lnot \alpha \rightarrow \alpha)\rightarrow \alpha)) & \quad \text{Ax}\,1.22.8 \\
	7. \quad && ((\lnot \alpha \rightarrow \alpha)\rightarrow(\lnot \alpha \rightarrow \alpha))\rightarrow((\lnot \alpha \rightarrow \alpha)\rightarrow \alpha) & \quad 5,6\,\text{MP} \\
	8. \quad && (\lnot \alpha \rightarrow \alpha) \rightarrow (\lnot \alpha \rightarrow \alpha) & \quad \text{slides 02v10 p8.16}\\
	9. \quad && (\lnot \alpha \rightarrow \alpha)\rightarrow \alpha & \quad 7,8\,\text{MP} \\
	10. \quad && \lnot \lnot \alpha \rightarrow (\lnot \alpha \rightarrow \alpha) & \quad \text{Ax}\,1.22.10 \\
	11. \quad && \lnot \lnot \alpha\vdash \alpha & \quad 9,10\,\text{三段论} \\
	\quad \tag*{Q.E.D}
\end{eqnarray*}
$$

### 2 证明
#### 1. 若$\Gamma$是不一致的，那么对于任意wff $\alpha$有$\Gamma \vdash \alpha$

证明：根据一致性的定义，由$\Gamma$不一致可知，$\Gamma \vdash \bot$. 根据公理1.22.12 对任意 $\alpha$ 有 $\vdash\bot\rightarrow\alpha$. 由以上两条结论与 MP 规则可得 $\Gamma\vdash\alpha$

#### 2. 若$\Gamma \vdash \alpha$且$\neg \alpha \in \Gamma$，那么$\Gamma$是不一致的

证明：由定理$1.30$知，$\Gamma \vdash \alpha$当且仅当$\Gamma \cup \{\neg \alpha\}$不一致，由$\neg \alpha \in \Gamma$知，$\Gamma \ \cup \{\neg \alpha\}=\Gamma$，即$\Gamma$是不一致的

#### 3. 若$\Gamma \cup \{\alpha\}$与$\Gamma \cup \{\neg \alpha\}$均不一致，那么$\Gamma$本身就不一致

证明： 由定理$1.30$可知：
1. $\Gamma \cup \{\neg\alpha\}$ 不一致当且仅当 $\Gamma\vdash\alpha$
2. 根据定义 $\Gamma\cup\{\alpha\}$ 不一致即为 $\Gamma\cup\{\alpha\}\vdash\bot$，根据演绎定理即 $\Gamma\vdash\alpha\rightarrow\bot$
3. 1, 2 根据 MP 规则可知 $\Gamma\vdash\bot$, 也即 $\Gamma$ 自身不一致


### 3 证明定理 I. 34
如果 $\Gamma$ 是完备 (complete) 且一致 (consistent) 的，那么：
#### 1. 若 $\Gamma \vdash \alpha$, 则 $\alpha \in \Gamma$

   可用反证法，若$\alpha\notin\Gamma$，由于 $\Gamma$ 是完备的，则由定义 I.33 可知 $\neg\alpha\in\Gamma$，由 $\vdash$ 的自反性可得 $\Gamma\vdash\neg\alpha$，但又有 $\Gamma\vdash\alpha$，这显然违反一致性，$\Gamma$ 不是一致的，与题设矛盾，得证。

#### 2. $\alpha \rightarrow \beta \in \Gamma$ 当且仅当要么 $\alpha \notin \Gamma$, 要么 $\beta \in \Gamma$

   - 必要性：已知 $\alpha\to\beta\in\Gamma$，可以用反证法证明，若能推出 “ $\alpha \in \Gamma$ 且 $\beta \notin \Gamma$”，则由 $\vdash$ 的自反性可得 $\Gamma\vdash\alpha\to\beta$ 及 $\Gamma\vdash\alpha$，利用 MP 规则有 $\Gamma\vdash\beta$，与第一小问证明类似，由 $\beta \notin \Gamma$ 及 $\Gamma$ 是完备的可知 $\Gamma\vdash\neg\beta$，违反一致性，$\Gamma$ 不是一致的，与题设矛盾，得证。
   - 充分性：分情况讨论之。
     若 $\alpha\notin\Gamma$，同理有 $\Gamma\vdash\neg\alpha$，又有公理 $\neg \alpha \rightarrow(\alpha \rightarrow \beta)$，利用 MP 规则可知 $\Gamma\vdash\alpha\to\beta$，由第一小问结论可知 $\alpha\to\beta \in \Gamma$；若 $\beta\in\Gamma$，同理有 $\Gamma\vdash\beta$，类似地，利用公理 $\beta \rightarrow(\alpha \rightarrow \beta)$ 可得 $\Gamma\vdash\alpha\to\beta$，进而有 $\alpha\to\beta \in \Gamma$。
   - 综上，得证。