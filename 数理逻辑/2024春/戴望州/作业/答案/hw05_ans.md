## 第五次作业

### 举例

#### 既不自反也不反自反：

- 自然数集上的二元关系$Pxy$：$x$和$y$的乘积为偶数
- $A=\{a, b\}$上的二元关系R：$R=\{(a, a), (a, b)\}$

#### 既不对称也不非对称：

- 自然数集上的二元关系$Pxy$：$x-y\ge 0$
- $A=\{a, b\}$上的二元关系R：$R=\{(a, a), (a, b)\}$

### 判断下列命题是否正确，并形式化为FOL来证明结论。若命题为假，只需要举一个反例即可。
#### 1. 若R是非对称的，那么它是自反的
形式化：$$\{\forall x\forall y(Rxy\rightarrow\neg Ryx\}\vdash\forall z\neg Rzz$$
**正确。**
利用演绎定理转换为：$\vdash(\forall x\forall y(Rxy\rightarrow\neg Ryx)\rightarrow\forall z\neg Rzz$

证明：
$$
\begin{eqnarray*}
	1. \quad && \forall x\forall y(Rxy\rightarrow\neg Ryx)\rightarrow \forall y(Rzy\rightarrow\neg Ryz) & \quad \text{Ax. 2.7.2}\\
	2. \quad && \forall y(Rzy\rightarrow\neg Ryz)\rightarrow (Rzz\rightarrow\neg Rzz) & \quad \text{Ax. 2.7.2}\\
	3. \quad && Rzz\rightarrow Rzz & \quad \text{slides 2.8.15}\\
	4. \quad && (Rzz\rightarrow Rzz) \rightarrow ((Rzz\rightarrow \lnot Rzz)\rightarrow \lnot Rzz) & \quad \text{Ax. 1.22.9}\\
	5. \quad && (Rzz\rightarrow \lnot Rzz)\rightarrow \lnot Rzz & \quad \text{3,4 MP} \\
	6. \quad && \forall x\forall y(Rxy\rightarrow\neg Ryx)\rightarrow\forall z\neg Rzz & \quad \text{1,2,5 三段论}\\
	\quad \tag*{Q.E.D}
\end{eqnarray*}
$$

#### 2. 若R是传递且反自反的，那么它是非对称的
形式化：$$\{\forall x \forall y \forall z(Rxy \wedge Ryz \rightarrow Rxz); \forall x \lnot Rxx\}\vdash \forall a\forall b(Rab\rightarrow\neg Rba)$$
**正确。**

证明：
$$
\begin{eqnarray*}
	1. \quad && \forall x \forall y \forall z(Rxy \wedge Ryz \rightarrow Rxz)\quad & \text{Hyp.} \\
	2. \quad && \forall x \forall y \forall z(Rxy \wedge Ryz \rightarrow Rxz) \rightarrow (Rab \wedge Rba \rightarrow Raa) \quad & \text{3 times Ax2.7.2: x,y,z}\rightarrow\text{a,b,a} \\
	3. \quad && Rab \wedge Rba \rightarrow Raa \quad & \text{1,2 MP}\\
	4. \quad && \lnot Raa \rightarrow \lnot(Rab \wedge Rba) \quad & \text{Contraposition} \\
	5. \quad && \forall x \lnot Rxx \quad & \text{Hyp.}\\
	6. \quad && \forall x \lnot Rxx \rightarrow \lnot Raa \quad & \text{Ax2.7.2: x}\rightarrow\text{a}\\
	7. \quad && \lnot(Rab \wedge Rba) \quad & \text{5,6,4 MP}\\
	8. \quad && \lnot(Rab \wedge Rba) \rightarrow \lnot Rab \vee\lnot Rba \quad & \text{Obviously} \\
	9. \quad && (\lnot Rab \vee\lnot Rba) \rightarrow (\lnot \lnot Rab \rightarrow \lnot Rba) \quad & \text{Obviousili}\\
	10. \quad && \lnot \lnot Rab \rightarrow \lnot Rba \quad & \text{7,8,9 MP}\\
	11. \quad && Rab \rightarrow \lnot Rba \quad & \text{Obviousily} \\
	12. \quad && (Rab \rightarrow \lnot Rba) \rightarrow \forall a \forall b(Rab \rightarrow \lnot Rba) \quad & \text{2 times Generalization}\\
	13. \quad && \forall a \forall b(Rab \rightarrow \lnot Rba) \quad & \text{11,12 MP} \\
	\quad \tag*{Q.E.D}
\end{eqnarray*}
$$

#### 3. 若 $R$ 是传递且对称的，那么它是自反的

形式化： 
$$ \vdash ( \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz) \wedge ( \forall x \forall y Rxy \rightarrow Ryx) ) \rightarrow \forall x Rxx$$

**错误。**

反例：考虑实数域上的关系 $R: \{(x, y) | xy > 0\}$，易验证$R$满足传递性和对称性，但不满足自反性（ $R00$ 不成立）

#### 4. 若 $R$ 是等价关系，那么它也是欧几里得关系

形式化：
$$ \vdash (\forall x Rxx \wedge \forall x \forall y ( Rxy \rightarrow Ryx ) \wedge \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz)) \rightarrow \forall x \forall y \forall z (Rxy \wedge Rxz \rightarrow Ryz) $$

**正确。**

根据演绎定理，证明上式等价于证明
$$ (\forall x Rxx \wedge \forall x \forall y ( Rxy \rightarrow Ryx ) \wedge \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz)) \vdash \forall x \forall y \forall z (Rxy \wedge Rxz \rightarrow Ryz) $$

即证
$$ \{\forall x Rxx, \forall x \forall y ( Rxy \rightarrow Ryx ), \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz) \}\vdash \forall x \forall y \forall z (Rxy \wedge Rxz \rightarrow Ryz) $$

根据概括定理和演绎定理，等价于证明：
$$ \{\forall x Rxx, \forall x \forall y ( Rxy \rightarrow Ryx ), \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz),Rxy, Rxz\}\vdash  Ryz) $$

证明：
$$
\begin{array}{llr}
1.& \forall x Rxx \quad & \text{Hyp} \\
2.& \forall x \forall y ( Rxy \rightarrow Ryx ) \quad & \text{Hyp} \\
3.&  \forall x \forall y \forall z ( Rxy \wedge Ryz \rightarrow Rxz) \quad & \text{Hyp} \\
4.&  Rxy & \text{Hyp} \\
5.&  Rxz & \text{Hyp} \\
6.&  Rxy \rightarrow Ryx & Ax2.7.2, 2, \text{MP} \\
7.&  Ryx & 4, 6,\text{MP} \\
8.&  Ryx \rightarrow (Rxz \rightarrow (Ryx \wedge Rxz)) &Ax1.22.3\\
9.&  Ryx \wedge Rxz \rightarrow Ryz & Ax2.7.2, 3, \text{MP} \\
10.&  Rxz \rightarrow Ryx \wedge Rxz & 7,8,\text{MP} \\
11.&  Ryx \wedge Rxz & 5, 10, \text{MP} \\
12.&  Ryz & 9,11,\text{MP}\\
\end{array}
$$

#### 5. 若 R 是欧几里得关系且是非对称的，那么它是反自反的 

**正确。**

由题 1 的证明可知，命题 “若 $R$ 是非对称的，那么它是反自反的” 正确，又根据 $\vdash$ 的单调性，有 “若 $R$ 是欧几里得关系且是非对称的，那么它是反自反的“ 成立。故该命题显然成立，具体证明方法与题 1 类似。

#### 6. 若 R 是欧几里得关系且是自反的，那么它是一个等价关系

**正确。**

根据演绎定理和等价关系等价于自反性、对称性、传递性，有该命题等价于下面三个命题：

1. $\vdash ((\forall x \forall y \forall z(Rxy \wedge Rxz \rightarrow Ryz \wedge Rzy)) \wedge (\forall x Rxx)) \rightarrow  \forall x Rxx$
2. $\vdash ((\forall x \forall y \forall z(Rxy \wedge Rxz \rightarrow Ryz \wedge Rzy)) \wedge (\forall x Rxx)) \rightarrow  \forall x \forall y (Rxy \rightarrow Ryx)$
3. $\vdash ((\forall x \forall y \forall z(Rxy \wedge Rxz \rightarrow Ryz \wedge Rzy)) \wedge (\forall x Rxx)) \rightarrow \forall x \forall y \forall z(Rxy \wedge Ryz \rightarrow Rxz)$

现依次证明命题 1、2、3：

1. 根据 $\alpha \vdash \alpha$ 和 $\vdash$ 的单调性，命题 1 显然成立。

2. 根据 $A X 2.7 .3$ 和演绎定理，该命题等价于：$$\{\forall x R xx, \forall x \forall y \forall z((R xy \wedge R xz) \rightarrow R yz), \forall x \forall yR xy\} \vdash \forall x\forall y R y x $$
	   则有：
	$$
	\begin{array}{rlr}
	1. & \forall x \forall y R xy & \text { Hyp. } \\
	2 . & \forall x \forall y R xy \rightarrow R xy & \text { AX } 2.7 .2 \\
	3. & R xy & 1,2 \mathrm{MP} \\
	4. & \forall x R xx & \text { Hyp. } \\
	5. & \forall x R x \rightarrow R xx & \text { AX } 2.7 .2 \\
	6 . & R xx& 4,5 \mathrm{MP} \\
	7 . & R xy \rightarrow(R xx \rightarrow(R xy \wedge Rxx)) & \text { Ax } 1.22 .3 \\
	8 . & R xx \rightarrow(R xy\wedge R xx) & 3,7 \mathrm{MP} \\
	9 . & R xy \wedge R xx & 6,8 \mathrm{MP} \\
	10 . & \forall x\forall y \forall z((R xy \wedge R x z) \rightarrow Ry z) & \text { Hyp. } \\
	11 . & \forall  x \forall y \forall z((R xy \wedge R x z) \rightarrow R y z) \rightarrow((R xy \wedge R xx) \rightarrow R yx) & \text { AX } 2.7 .2 \\
	12 . & (Rxy \wedge R xx) \rightarrow R yx & 10,11 \mathrm{MP} \\
	13.& R yx & 9,12 \mathrm{MP} \\
	14. & \forall x \forall y R yx & \text { Gen. }
	\end{array}
	$$
	
	命题 2 成立。

3. 根据 $A X 2.7 .3$ 和演绎定理，该命题等价于：$$\{\forall x R xx, \forall x\forall y \forall z((R xy \wedge R x z ) \rightarrow R y z), \forall x \forall y \forall z(R x y \wedge R y z)\} \vdash \forall x \forall z R x z$$
   则有：
   $$
   \begin{array}{rlr}
   
   1.&  \forall x \forall y \forall z(R x y \wedge R y z) &  \text{Hyp.} \\
   2.&  \forall x \forall y \forall z(R x y \wedge R y z) \rightarrow (R x y \wedge R y z) &  \text{AX 2.7 .2} \\
   3.&  R x y \wedge R y z &  1,2 \text{ MP} \\
   4.&  (R x y \wedge R y z) \rightarrow R x y &  \text{Ax 1.22 .1} \\
   5.&  (R x y \wedge R y z) \rightarrow R y z & \text{Ax 1.22 .2} \\
   6.&  R x y &  3,4 \text{ MP} \\
   7.&  R y z &  3,5 \text{ MP} \\
   8.&  \forall x \forall y(R x y \rightarrow R y x) &  \text{ 命题 2} \\
   9.&  \forall x \forall y(R x y \rightarrow R y x) \rightarrow (R x y \rightarrow R y x) &  \text{AX 2.7 .2} \\
   10.&  R x y \rightarrow R y x & 8,9 \text{ MP} \\
   11.&  R y x & 6,10 \text{ MP} \\
   12.&  R y x \rightarrow (R y z \rightarrow (R y x \wedge R y z)) &  \text{Ax 1.22 .3} \\
   13.&  R y z \rightarrow (R y x \wedge R y z) &  11,12 \text{ MP} \\
   14.&  R y x \wedge R y z &  7,13 \text{ MP} \\
   15.& \forall x \forall y \forall z((R y x \wedge R y z) \rightarrow R x z) &  \text{Hyp.} \\
   16.&  \forall x \forall y \forall z((R y x \wedge R y z) \rightarrow R x z) \rightarrow ((R y x \wedge R y z) \rightarrow R x z) &  \text{AX 2.7 .2} \\
   17.&   (R y x \wedge R y z) \rightarrow R x z &  15,16 \text{ MP} \\
   18.&  R x z &  14,17 \text{ MP} \\
   19.&  \forall x \forall z R x z &  \text{Gen.}
   \end{array}
   $$
   命题 3 成立。