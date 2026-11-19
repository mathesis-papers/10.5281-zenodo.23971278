# 精确陈述与证明

以下 $n$ 总是非负整数，$0!=1$。原文的 Theorem 1 与 Corollaries 2–6 依次对应本章六个结果。$S(n)$ 为 $n$ 的二进制占据位置集合；“四分离”指任意 $i<j$ 属于 $S(n)$ 时均有 $j-i\geq4$，空集也满足。定义


$$
a(n)=\frac{(15n)!(2n)!}{(10n)!(6n)!n!}.
$$


::: {.theorem #thm-parity title="自然数实现与奇偶性" lean="D5/S3/Arith/FactorialRatio/BalaA295462Parity.result" mathesis="collected:bala295462:4:s1"}
对每个 $n$，存在自然数 $m$，使 $a(n)=m$（在有理数中），且 $m$ 是奇数当且仅当 $S(n)$ 四分离。
:::


原文还陈述 $a(n)>0$：所有阶乘均为正，分母不为零，故该自然数实现严格为正。此处将这一步初等推论与上框中形式声明的字面结论分开。


::: {.proof #pf-parity}
令

$$
\begin{aligned}
F(x)={}&\lfloor15x\rfloor+\lfloor2x\rfloor\\
&-\lfloor10x\rfloor-\lfloor6x\rfloor-\lfloor x\rfloor.
\end{aligned}
$$

系数平衡给出 $F(x+1)=F(x)$。对 $0\leq j<30$，在半开区间 $[j/30,(j+1)/30)$ 上，$F$ 等于 $\lfloor j/2\rfloor+\lfloor j/15\rfloor-\lfloor j/3\rfloor-\lfloor j/5\rfloor$。按每十项分组，其值为

$$
\begin{aligned}
&(0,0,1,0,1,0,0,0,1,0),\\
&(0,0,0,0,1,0,1,1,1,1),\\
&(1,0,1,1,1,0,1,0,1,1).
\end{aligned}
$$

因此 $F\geq0$，包括每个跳点。Legendre 公式给出 $v_p(a(n))=\sum_{k\geq1}F(n/p^k)$，且 $p^k>15n$ 时项为零。正有理数的各素数赋值均非负，故它是整数；$n=0$ 时为 $1$。对于 $p=2$，总和为零当且仅当每项为零。

在四分离情形，位于 $e$ 以下且与 $e$ 至少相距四位的尾部满足

$$
0\leq R\leq\sum_{j\geq1,\ e-4j\geq0}2^{e-4j}<2^e/15.
$$

固定 $k\geq1$，令 $r=n\bmod2^k$。若 $r=0$，$F(r/2^k)=0$；否则写 $r=2^t+R$，$t<k$，并令 $\ell=k-t$。于是 $x=r/2^k=(1+u)/2^\ell$，$0\leq u<1/15$。下面每个五元组按 $\lfloor15x\rfloor,\lfloor2x\rfloor,\lfloor10x\rfloor,\lfloor6x\rfloor,\lfloor x\rfloor$ 排列：

- $\ell=1$：$(7,1,5,3,0)$；
- $\ell=2$：$(3,0,2,1,0)$；
- $\ell=3$：$(1,0,1,0,0)$；
- $\ell\geq4$：$(0,0,0,0,0)$。

它们均给出 $F(x)=0$；周期性使这等于 $F(n/2^k)$。

若不四分离，取最低的、在前三位内有前驱的占据位置 $t$，其紧邻的低位前驱为 $e$。$d=t-e\in\{1,2,3\}$。由 $t$ 的最小性，更低部分仍四分离，故

$$
\begin{aligned}n\bmod2^{t+1}&=(2^d+1)2^e+R,\\0&\leq15R<2^e.\end{aligned}
$$

在 $x=(2^d+1+u)/2^{d+1}$、$0\leq u<1/15$ 处，三个五元组依次为 $(11,1,7,4,0)$、$(9,1,6,3,0)$、$(8,1,5,3,0)$。每组给出 $F(x)=1$，所以 $v_2(a(n))\geq1$。这证明两个方向。来源：原文 §2，Theorem 1 的证明；对应的完整形式证明见上框源码。
:::


::: {.corollary #cor-2 title="除去两个奇因子" status="written-proof" proof="pf-2" doi="10.5281/zenodo.23971279" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/264" mathesis="collected:bala295462:4:s2"}
$b(n)=a(n)/((6n+1)(10n+1))$ 对所有 $n\geq0$ 均为正整数，且为奇数当且仅当 $S(n)$ 四分离。
:::


::: {.proof #pf-2}
这是原文 §3 的 Corollary 2，整除性归于 Bala（2026）。令 $h=6$ 或 $10$。对素数 $p\mid hn+1$，有 $\gcd(p,h)=1$。每当 $1\leq r\leq v_p(hn+1)$，令 $m=p^r$、$s=n\bmod m$。可写 $hs=qm-1$，其中 $1\leq q<h$、$\gcd(q,h)=1$，所以 $s/m=q/h-1/(hm)$。$h=6$ 时 $m\geq5$、$q=1,5$；$h=10$ 时 $m\geq3$、$q=1,3,7,9$。代入 $F$，按刚才的五元组顺序：

- $(h,q)=(6,1)$：$(2,0,1,0,0)$；$(6,5)$：$(12,1,8,4,0)$；
- $(10,1)$：$(1,0,0,0,0)$；$(10,3)$：$(4,0,2,1,0)$；
- $(10,7)$：$(10,1,6,4,0)$；$(10,9)$：$(13,1,8,5,0)$。

每行均给出 $F(s/m)=1$，最小允许的 $m$ 端点也在内。因此 $v_p(a(n))\geq v_p(hn+1)$，即 $hn+1\mid a(n)$。两个除数均为奇数，公因子整除 $5(6n+1)-3(10n+1)=2$，故互素，乘积也整除 $a(n)$。商为正且除数为奇数，故 $v_2(b(n))=v_2(a(n))$；应用 [@thm-parity] 即得。$n=0$ 时商为 $1$。
:::


::: {.corollary #cor-3 title="计数与按序生成" status="written-proof" proof="pf-3" doi="10.5281/zenodo.23971279" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/265" mathesis="collected:bala295462:4:s3"}
令 $c_m$ 计数 $0\leq n<2^m$ 中 $a(n)$ 为奇数的输入。则

$$
\begin{aligned}
c_0=1,\ c_1=2,\ c_2=3,\ c_3=4,\\
c_m=c_{m-1}+c_{m-4}\quad(m\geq4).
\end{aligned}
$$

令 $u_0,u_1,\ldots$ 按递增顺序列出这些输入。$u_0=0$；对 $j>0$，存在唯一 $e\geq0$ 使 $c_e\leq j<c_{e+1}$，且

$$
u_j=2^e+u_{j-c_e}.
$$
:::


::: {.proof #pf-3}
原文 §3，Corollary 3。由 [@thm-parity]，只需数四分离二进制串。允许前导零，长度 $0,1,2,3$ 的合法串分别有 $1,2,3,4$ 个；长度 $m\geq4$ 时，开头 $0$ 留下长度 $m-1$ 的合法串，开头 $1$ 则必须接 $000$，留下长度 $m-4$ 的合法串。两类不交且穷尽，得到递推。

$c_m$ 严格递增，因为 $2^m$ 是新增的合法输入；并且趋于无穷，因为所有单一 $1$ 的串均合法，故上述 $e$ 唯一存在。小于 $2^e$ 的合法输入恰有 $c_e$ 个。位于 $[2^e,2^{e+1})$ 的合法输入，在 $e\geq3$ 时恰为 $2^e$ 加上所有小于 $2^{e-3}$ 的合法尾部；$e<3$ 时尾部只能为零。区块内部次序与尾部次序相同，故索引减去 $c_e$ 后给出递推。
:::


::: {.corollary #cor-4 title="四位窗口与十一条 XOR 恒等式" status="written-proof" proof="pf-4" doi="10.5281/zenodo.23971279" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/266" mathesis="collected:bala295462:4:s4"}
若 $a(n)$ 为奇数，则对 $0\leq u,v<16$，

$$
(un)\oplus(vn)=(u\oplus v)n.
$$

把 XOR 全部换成 AND 或 OR，等式仍成立。以下每个三元组 $(u,v,w)$ 也满足 $(un)\oplus(vn)=wn$：

$$
\begin{gathered}
(1,14,15),\ (3,9,10),\ (3,13,14),\\
(5,9,12),\ (5,11,14),\ (6,11,13),\\
(7,9,14),\ (7,10,13),\ (7,11,12),\\
(12,21,25),\ (12,37,41).
\end{gathered}
$$
:::


::: {.proof #pf-4}
原文 §4，Corollary 4；十一条恒等式归于 Hanna（2006），Karlsson（2022）已有 Walnut 验证。由 [@thm-parity]，$S=S(n)$ 四分离。$un=\sum_{e\in S}u2^e$ 的四位块互不重叠，故三种按位运算逐块进行。这给出一般公式与前九个三元组。

对最后两个三元组，取 $k=4$ 或 $5$，令 $z=n+2^kn$。集合 $S\cup(S+k)$ 与 $(S+2)\cup(S+3)$ 不交：任何交点都会让 $S$ 中两个位置距离为 $1,2,3$。加法中的碰撞仅发生在 $t\in S\cap(S+k)$，产生位于 $t+1$ 的进位。$t+1$ 不在 $S$，否则与 $t$ 相邻；也不在 $S+k$，否则 $t+1-k$ 与 $t-k$ 在 $S$ 中相邻。因此进位一步停止。进位位置也不属于 $S+2$ 或 $S+3$，因为那会让 $S$ 中某位置与 $t$ 相距 $1$ 或 $2$。所以 $z,4n,8n$ 的支撑两两不交，且

$$
(z+4n)\oplus(z+8n)=12n.
$$

两个输入分别是 $(21n,25n)$ 与 $(37n,41n)$。利用 XOR 的结合律及 $x\oplus x=0$，再异或 $12n$ 即得所列三元组。$n=0$ 也在内。源文末尾还指出：对任意 $r\geq1$，$r$ 分离的支撑与掩码 $u,v<2^r$ 有同样的逐块 XOR/AND/OR 公式，因为每块长度为 $r$ 且互不重叠。
:::


## 任意长度的乘积

令 $L_R=\operatorname{lcm}(1,\ldots,R)$，$R\geq1$，并定义


$$
T(n)=\frac{(12n)!n!}{(6n)!(4n)!(3n)!}.
$$


::: {.corollary #cor-families title="固定整除性与两个乘积族" lean="D5/S3/Arith/FactorialRatio/BalaA295431Divisibility.result" mathesis="collected:bala295462:4:s5"}
以下五个表达式对所有 $n\geq0$ 均为整数。取下列常数后，最后两个表达式对所有 $R\geq1$、$n\geq0$（第一族另有 $k=1,2,3$）也均为整数。

$$
\begin{gathered}
\frac{385T(n)}{n+1},\quad \frac{5T(n)}{2n+1},\\
\frac{T(n)}{3n+1},\quad \frac{T(n)}{12n-1},\\
\frac{770T(n)}{(n+1)(2n+1)(3n+1)}.
\end{gathered}
$$

$$
\begin{aligned}
C(k,R)&=36(R-1)!L_{12R}\quad(k=1,2,3),\\
D(R)&=(R-1)!L_R.
\end{aligned}
$$

$$
\frac{C(k,R)T(n)}{\prod_{i=1}^R(kn+i)},
$$

$$
\frac{D(R)T(n)}{\prod_{\substack{1\leq i\leq R\\\gcd(i,12)=1}}(12n-i)}.
$$

所有分母均非零；带符号的因子按整数解释，$T(0)/(12\cdot0-1)=-1$。
:::


::: {.proof #pf-families}
原文 §5，Corollary 5；对应形式证明直接覆盖上框的所有量词与表达式。下面解释统一常数的机制。令

$$
\begin{aligned}
G(x)={}&\lfloor12x\rfloor+\lfloor x\rfloor\\
&-\lfloor6x\rfloor-\lfloor4x\rfloor-\lfloor3x\rfloor.
\end{aligned}
$$

它周期为 $1$，十二个半开 $1/12$ 小区间的值依次为 $(0,1,1,1,0,1,0,1,0,0,0,1)$。因此 $T(n)$ 是正整数，$v_p(T(n))=\sum_{j\geq1}G(n/p^j)$；$p^j>12n$ 时项为零。

固定表达式的关键是检查 $p^j\mid hn+1$ 对应的左侧小区间。对 $p\geq5$，$h=1$ 仅在 $p^j=5,7,11$ 时缺一个单位，$h=2$ 仅在 $p^j=5$ 时缺一个，$h=3$ 没有缺口。它们解释了 $385=5\cdot7\cdot11$ 与 $5$。对小素数，Legendre 公式给出

$$
\begin{aligned}
v_2(T(n))&=s_2(3n),\\
v_3(T(n))&=s_3(2n)/2,
\end{aligned}
$$

其中 $s_p$ 是 $p$ 进制数字和。$n+1=2^ra$、$r\geq2$ 时，$3n$ 的末 $r$ 位为 $2^r-3$，重量 $r-1$，正前缀 $3a-1$ 再提供至少一个 $1$；$r=1$ 直接成立。若 $2^r\mid3n+1$，末 $r$ 位全为 $1$。$n+1=3^ra$ 时，$2n$ 的末 $r$ 个三进制位数字和为 $2r-1$，正前缀再补至少 $1$；若 $3^r\mid2n+1$，这些位全为 $2$。这补齐前三个表达式。三个分母除 $n+1$ 与 $3n+1$ 可公含一个额外的 $2$ 外互素；它们同时为偶数时其中一个的二进制赋值为 $1$。模 $5$ 的两个缺口又在不同剩余类，因此 $770=2\cdot385$ 足够。对 $p^j\mid12n-1$，$p\geq5$，相应点从 $q/12$ 右侧接近，$q=1,5,7,11$，每次 $G=1$，证明了分母为 $12n-1$ 的式子为整数。

对一般乘积，取分母中 $p$ 赋值最大的因子，赋值记为 $e$，索引为 $i_0$。其他因子的赋值不超过 $v_p(i-i_0)$：减去最大因子即可，赋值相同的情形也满足这个不等式。相关差的乘积整除 $(i_0-1)!(R-i_0)!$，后者整除 $(R-1)!$。子集与负因子亦如此。因此

$$
v_p(\text{分母乘积})\leq e+v_p((R-1)!).
$$

在第一族中，令 $E_p=\lfloor\log_p(12R)\rfloor$。当 $p\geq5$、$p^j>12R$ 且 $p^j\mid kn+i$ 时，剩余小数是 $q/k-i/(kp^j)$，落在 $1/3,1/2,2/3,1$ 左侧宽 $1/12$ 的区间，故 $G=1$。于是 $v_p(T(n))\geq e-E_p$。对 $p=2,3$，数字和恒等式

$$
s_p(p^j-d)=(p-1)j-s_p(d-1)
$$

用于 $3n\equiv-3i,-i\pmod{2^j}$ 与 $2n\equiv-2i,-i\pmod{3^j}$，其中 $d\leq3R$。若 $p^j\leq d$，则 $j\leq E_p$；否则 $s_p(d-1)\leq(p-1)(E_p+1)$。剩下 $k=p$ 的情形，$p\nmid i$ 时赋值为零；$i=ph$ 时提取一个 $p$，至多再损失一个单位。因此两小素数均有 $v_p(T(n))\geq e-E_p-2$。$L_{12R}$ 补上 $E_p$，$36=2^23^2$ 补上两个小素数的余量，$(R-1)!$ 处理其他因子。

在第二族中，各因子与 $6$ 互素。若 $p^j>R$ 且 $p^j\mid12n-i$，相应点为 $q/12+i/(12p^j)$，$q\in\{1,5,7,11\}$，落在 $G=1$ 的右侧小区间。所以 $v_p(T(n))\geq e-\lfloor\log_pR\rfloor$，由 $L_R$ 和同一乘积界即可补齐。$12n-i=0$ 与 $\gcd(i,12)=1$ 矛盾，故无零分母。
:::


::: {.corollary #cor-6 title="系数公式与增长" status="written-proof" proof="pf-6" doi="10.5281/zenodo.23971279" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/267" mathesis="collected:bala295462:4:s6"}
A295462 与 A295431 中的二项式恒等式、超几何级数与渐近公式均成立，A295431 中 Mathar 的递推亦成立。下面的证明明确列出原文 §6、Corollary 6 所指的全部公式及其定义。
:::


::: {.proof #pf-6}

原文 §6，Corollary 6。展开阶乘，直接得到 Chai Wah Wu 在 A295462 的两式：


$$
a(n)=\frac{\binom{15n}{5n}\binom{2n}{n}}{\binom{6n}{n}},
$$


$$
a(n)=\frac{\binom{15n}{5n}\binom{7n}{n}}{\binom{7n}{2n}}.
$$

令以下集合的所有元素分别除以 $15$，并定义参数：


$$
\begin{aligned}A&=\{1,2,4,7,8,11,13,14\}/15,\\B=\{&1/10,1/6,3/10,1/2,\\&7/10,5/6,9/10\},\\C&=61509375/16384.\end{aligned}
$$


$$
\frac{a(n+1)}{a(n)}=\frac{C\prod_{\alpha\in A}(n+\alpha)}{(n+1)\prod_{\beta\in B}(n+\beta)}.
$$

此比值由相邻阶乘相消得到，且 $C=15^{15}2^2/(10^{10}6^6)$。定义上升阶乘 $(q)_0=1$、$(q)_n=q(q+1)\cdots(q+n-1)$；超几何级数 ${}_pF_q(A;B;z)$ 的第 $n$ 项是 $\prod_{\alpha\in A}(\alpha)_n\,z^n/(n!\prod_{\beta\in B}(\beta)_n)$。初值 $a(0)=1$ 与比值唯一决定系数，故作为形式幂级数有


$$
\sum_{n\geq0}a(n)z^n={}_8F_7(A;B;Cz).
$$

Stirling 公式给出 Amiram Eldar 在 A295462 记录的渐近式：


$$
a(n)\sim\frac1{2\sqrt{\pi n}}\left(\frac{3^95^5}{2^{14}}\right)^n\quad(n\to\infty).
$$

其中指数因子 $e^{-kn}$ 相消，$n$ 的幂留下 $n^{-1/2}$，根号常数为 $\sqrt{30/60}/\sqrt{2\pi n}=1/(2\sqrt{\pi n})$。

对 $T(n)$，同样的阶乘消去给出 Wu 在 A295431 的两式：


$$
T(n)=\frac{\binom{12n}{6n}\binom{6n}{2n}}{\binom{3n}{n}},
$$


$$
T(n)=\frac{\binom{12n}{6n}\binom{7n}{3n}}{\binom{7n}{n}}.
$$

相邻项的比值如下，即 Mathar 的递推（$n\geq1$）：


$$
\begin{aligned}\frac{T(n)}{T(n-1)}={}&\frac{24(12n-11)(12n-1)}{n(3n-1)}\\&\cdot\frac{(12n-5)(12n-7)}{(2n-1)(3n-2)}.\end{aligned}
$$

由 $T(0)=1$ 与同样的系数比值得到形式生成函数；将参数写成两行：


$$
\begin{aligned}A_T&=(1/12,5/12,7/12,11/12),\\B_T&=(1/3,1/2,2/3).\end{aligned}
$$


$$
\sum_{n\geq0}T(n)z^n={}_4F_3(A_T;B_T;27648z).
$$

最后，Penson 的展开是（$n\to\infty$）


$$
\begin{aligned}T(n)=\frac{27648^n}{\sqrt{12\pi n}}\bigg(&1+\frac1{36n}\\&+\frac1{2592n^2}+O(n^{-3})\bigg).\end{aligned}
$$

由 Stirling 对数展开，根号前因子为 $1/\sqrt{12\pi n}$，$1/n$ 的系数为 $(1/12+1-1/6-1/4-1/3)/12=1/36$。对数中没有 $1/n^2$ 项，指数化后产生 $1/(2\cdot36^2)=1/2592$；Stirling 余项在此给出 $O(n^{-3})$。形式级数恒等式不要求先选择收敛点；渐近式只在正整数 $n\to\infty$ 时使用，不代入 $n=0$。

:::
