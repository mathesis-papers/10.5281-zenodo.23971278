# Statements and proofs

Throughout, $n$ is a nonnegative integer and $0!=1$. The six results below correspond to source Theorem 1 and Corollaries 2–6. Put $S(n)$ for the set of occupied binary positions of $n$. It is four-separated when $j-i\geq4$ for all $i<j$ in $S(n)$, including the empty set. Define


$$
a(n)=\frac{(15n)!(2n)!}{(10n)!(6n)!n!}.
$$


::: {.theorem #thm-parity title="Natural realization and parity" lean="D5/S3/Arith/FactorialRatio/BalaA295462Parity.result" mathesis="collected:bala295462:4:s1"}
For every $n$, there is a natural number $m$ with $a(n)=m$ in the rationals, and $m$ is odd if and only if $S(n)$ is four-separated.
:::


The source also states $a(n)>0$: every factorial is positive and the denominator is nonzero, so this natural realization is strictly positive. This elementary consequence is separated here from the literal conclusion of the formal declaration above.


::: {.proof #pf-parity}
Put

$$
\begin{aligned}
F(x)={}&\lfloor15x\rfloor+\lfloor2x\rfloor\\
&-\lfloor10x\rfloor-\lfloor6x\rfloor-\lfloor x\rfloor.
\end{aligned}
$$

Balance of the coefficients gives $F(x+1)=F(x)$. On the half-open cell $[j/30,(j+1)/30)$, $0\leq j<30$, its value is $\lfloor j/2\rfloor+\lfloor j/15\rfloor-\lfloor j/3\rfloor-\lfloor j/5\rfloor$. In groups of ten, these values are

$$
\begin{aligned}
&(0,0,1,0,1,0,0,0,1,0),\\
&(0,0,0,0,1,0,1,1,1,1),\\
&(1,0,1,1,1,0,1,0,1,1).
\end{aligned}
$$

Thus $F\geq0$, including the jump points. Legendre's formula gives $v_p(a(n))=\sum_{k\geq1}F(n/p^k)$, with zero terms for $p^k>15n$. A positive rational with all prime valuations nonnegative is an integer; at $n=0$ it equals $1$. For $p=2$, the sum vanishes exactly when every summand vanishes.

For four-separated support, a tail below position $e$ and at least four positions away satisfies

$$
0\leq R\leq\sum_{j\geq1,\ e-4j\geq0}2^{e-4j}<2^e/15.
$$

Fix $k\geq1$ and put $r=n\bmod2^k$. If $r=0$, then $F(r/2^k)=0$. Otherwise write $r=2^t+R$, $t<k$, and $\ell=k-t$. Then $x=r/2^k=(1+u)/2^\ell$ with $0\leq u<1/15$. The five-tuples below list $\lfloor15x\rfloor,\lfloor2x\rfloor,\lfloor10x\rfloor,\lfloor6x\rfloor,\lfloor x\rfloor$:

- $\ell=1$: $(7,1,5,3,0)$;
- $\ell=2$: $(3,0,2,1,0)$;
- $\ell=3$: $(1,0,1,0,0)$;
- $\ell\geq4$: $(0,0,0,0,0)$.

Every row gives $F(x)=0$; periodicity identifies it with $F(n/2^k)$.

If the support is not four-separated, choose the lowest occupied position $t$ with a predecessor among the previous three positions, and let $e$ be its immediately preceding occupied position. Then $d=t-e\in\{1,2,3\}$. Minimality of $t$ makes the lower part four-separated, so

$$
\begin{aligned}n\bmod2^{t+1}&=(2^d+1)2^e+R,\\0&\leq15R<2^e.\end{aligned}
$$

At $x=(2^d+1+u)/2^{d+1}$, $0\leq u<1/15$, the three five-tuples are $(11,1,7,4,0)$, $(9,1,6,3,0)$ and $(8,1,5,3,0)$. Each gives $F(x)=1$, so $v_2(a(n))\geq1$. This proves both directions. Source: §2, proof of Theorem 1; the linked declaration supplies the complete formal proof.
:::


::: {.corollary #cor-2 title="Removing two odd factors" status="written-proof" proof="pf-2" doi="10.5281/zenodo.23971279" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/264" mathesis="collected:bala295462:4:s2"}
$b(n)=a(n)/((6n+1)(10n+1))$ is a positive integer for every $n\geq0$, and is odd if and only if $S(n)$ is four-separated.
:::


::: {.proof #pf-2}
This is source Corollary 2 in §3; the divisibilities are attributed to Bala (2026). Let $h=6$ or $10$. If a prime $p$ divides $hn+1$, then $\gcd(p,h)=1$. For each $1\leq r\leq v_p(hn+1)$, put $m=p^r$ and $s=n\bmod m$. Write $hs=qm-1$, where $1\leq q<h$ and $\gcd(q,h)=1$. Thus $s/m=q/h-1/(hm)$. For $h=6$, $m\geq5$ and $q=1,5$; for $h=10$, $m\geq3$ and $q=1,3,7,9$. Substitution into $F$, in the preceding five-tuple order, gives:

- $(h,q)=(6,1)$: $(2,0,1,0,0)$; $(6,5)$: $(12,1,8,4,0)$;
- $(10,1)$: $(1,0,0,0,0)$; $(10,3)$: $(4,0,2,1,0)$;
- $(10,7)$: $(10,1,6,4,0)$; $(10,9)$: $(13,1,8,5,0)$.

Every row gives $F(s/m)=1$, including the smallest allowed endpoint $m$. Hence $v_p(a(n))\geq v_p(hn+1)$, proving $hn+1\mid a(n)$. The two divisors are odd and any common divisor divides $5(6n+1)-3(10n+1)=2$. They are coprime, so their product divides $a(n)$. The quotient is positive and its divisor odd, giving $v_2(b(n))=v_2(a(n))$. Apply [@thm-parity]. At $n=0$ the quotient is $1$.
:::


::: {.corollary #cor-3 title="Counting and ordered enumeration" status="written-proof" proof="pf-3" doi="10.5281/zenodo.23971279" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/265" mathesis="collected:bala295462:4:s3"}
Let $c_m$ count inputs $0\leq n<2^m$ with odd $a(n)$. Then

$$
\begin{aligned}
c_0=1,\ c_1=2,\ c_2=3,\ c_3=4,\\
c_m=c_{m-1}+c_{m-4}\quad(m\geq4).
\end{aligned}
$$

List these inputs in increasing order as $u_0,u_1,\ldots$. Then $u_0=0$. For $j>0$ there is a unique $e\geq0$ with $c_e\leq j<c_{e+1}$, and

$$
u_j=2^e+u_{j-c_e}.
$$
:::


::: {.proof #pf-3}
Source §3, Corollary 3. By [@thm-parity], count four-separated binary words. Allowing leading zeros, the counts at lengths $0,1,2,3$ are $1,2,3,4$. At length $m\geq4$, an initial $0$ leaves any valid word of length $m-1$; an initial $1$ must be followed by $000$, leaving any valid word of length $m-4$. These disjoint cases exhaust the possibilities.

The counts strictly increase because $2^m$ is a new valid input, and are unbounded because every single-one word is valid. Thus $e$ exists uniquely. Exactly $c_e$ valid inputs lie below $2^e$. For $e\geq3$, those in $[2^e,2^{e+1})$ are precisely $2^e$ plus valid suffixes below $2^{e-3}$; for $e<3$, only the zero suffix is possible. Their internal order is the suffix order, so subtracting $c_e$ from the enumeration index proves the recursion.
:::


::: {.corollary #cor-4 title="Four-bit windows and eleven XOR identities" status="written-proof" proof="pf-4" doi="10.5281/zenodo.23971279" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/266" mathesis="collected:bala295462:4:s4"}
If $a(n)$ is odd, then for $0\leq u,v<16$,

$$
(un)\oplus(vn)=(u\oplus v)n.
$$

The same identity holds with XOR replaced throughout by AND or OR. Each triple $(u,v,w)$ below also satisfies $(un)\oplus(vn)=wn$:

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
Source §4, Corollary 4. The eleven identities are attributed to Hanna (2006), with earlier Walnut verification by Karlsson (2022). By [@thm-parity], $S=S(n)$ is four-separated. The four-bit blocks in $un=\sum_{e\in S}u2^e$ are disjoint, so all three bitwise operations act block by block. This proves the general formulas and the first nine triples.

For the final two triples take $k=4$ or $5$ and put $z=n+2^kn$. The sets $S\cup(S+k)$ and $(S+2)\cup(S+3)$ are disjoint: an intersection would put two positions of $S$ at distance $1,2$ or $3$. A collision in the addition occurs only at $t\in S\cap(S+k)$ and creates a carry at $t+1$. This position is not in $S$, since it would be adjacent to $t$, or in $S+k$, since then $t+1-k$ would be adjacent to $t-k$ in $S$. Every carry therefore stops after one position. A carry position also avoids $S+2$ and $S+3$, since otherwise a position of $S$ would be at distance $1$ or $2$ from $t$. Hence $z,4n,8n$ have pairwise disjoint supports, and

$$
(z+4n)\oplus(z+8n)=12n.
$$

The pairs are $(21n,25n)$ and $(37n,41n)$. Associativity of XOR and $x\oplus x=0$ give the listed triples after XORing again with $12n$. This includes $n=0$. The source also observes that, for every $r\geq1$, $r$-separated support and masks $u,v<2^r$ obey the corresponding blockwise XOR/AND/OR formulas: their blocks have length $r$ and are disjoint.
:::


## Products of arbitrary length

Let $L_R=\operatorname{lcm}(1,\ldots,R)$ for $R\geq1$, and define


$$
T(n)=\frac{(12n)!n!}{(6n)!(4n)!(3n)!}.
$$


::: {.corollary #cor-families title="Fixed divisibilities and two product families" lean="D5/S3/Arith/FactorialRatio/BalaA295431Divisibility.result" mathesis="collected:bala295462:4:s5"}
The following five expressions are integers for every $n\geq0$. With the constants displayed below, the final two expressions are also integers for every $R\geq1$ and $n\geq0$ (and $k=1,2,3$ in the first family).

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

All denominators are nonzero. Signed factors are interpreted in the integers, and $T(0)/(12\cdot0-1)=-1$.
:::


::: {.proof #pf-families}
Source §5, Corollary 5. The linked formal proof covers every displayed expression and quantifier. Here is the mechanism behind the uniform constants. Put

$$
\begin{aligned}
G(x)={}&\lfloor12x\rfloor+\lfloor x\rfloor\\
&-\lfloor6x\rfloor-\lfloor4x\rfloor-\lfloor3x\rfloor.
\end{aligned}
$$

It has period one and values $(0,1,1,1,0,1,0,1,0,0,0,1)$ on the twelve half-open cells of length $1/12$. Thus $T(n)$ is a positive integer and $v_p(T(n))=\sum_{j\geq1}G(n/p^j)$; terms vanish when $p^j>12n$.

For the fixed expressions, inspect the left-hand cells forced by $p^j\mid hn+1$. For $p\geq5$, $h=1$ misses one unit only at $p^j=5,7,11$; $h=2$ misses one only at $p^j=5$; $h=3$ has no missing levels. These explain $385=5\cdot7\cdot11$ and $5$. At the small primes Legendre's formula gives

$$
\begin{aligned}
v_2(T(n))&=s_2(3n),\\
v_3(T(n))&=s_3(2n)/2,
\end{aligned}
$$

where $s_p$ is the base-$p$ digit sum. If $n+1=2^ra$, $r\geq2$, the last $r$ bits of $3n$ are $2^r-3$, of weight $r-1$, and the positive prefix $3a-1$ supplies another one; $r=1$ is immediate. If $2^r\mid3n+1$, the last $r$ bits are all one. If $n+1=3^ra$, the last $r$ ternary digits of $2n$ sum to $2r-1$, and the positive prefix supplies at least one more. If $3^r\mid2n+1$, those digits are all two. This completes the first three expressions. The three denominators are pairwise coprime except for a possible extra factor of two shared by $n+1$ and $3n+1$; when both are even, one has binary valuation one. The two missing levels modulo five occur in distinct residue classes, so $770=2\cdot385$ suffices. If $p^j\mid12n-1$, then $p\geq5$ and the point approaches $q/12$ from the right, $q=1,5,7,11$, always giving $G=1$. This proves integrality of the expression with denominator $12n-1$.

For a general denominator product, select a factor with maximal $p$-valuation $e$, at index $i_0$. Every other factor has valuation at most $v_p(i-i_0)$, by subtracting the maximal factor; equal valuations also satisfy this bound. The product of the relevant differences divides $(i_0-1)!(R-i_0)!$, which divides $(R-1)!$. This works for subsets and signed factors as well. Writing $P$ for the denominator product, we obtain

$$
v_p(P)\leq e+v_p((R-1)!).
$$

For the first family put $E_p=\lfloor\log_p(12R)\rfloor$. If $p\geq5$, $p^j>12R$ and $p^j\mid kn+i$, the fractional residue is $q/k-i/(kp^j)$, in a left-hand interval of width $1/12$ at $1/3,1/2,2/3$ or $1$. Thus $G=1$ and $v_p(T(n))\geq e-E_p$. For $p=2,3$, use

$$
s_p(p^j-d)=(p-1)j-s_p(d-1)
$$

on $3n\equiv-3i,-i\pmod{2^j}$ and $2n\equiv-2i,-i\pmod{3^j}$, with $d\leq3R$. If $p^j\leq d$, then $j\leq E_p$; otherwise $s_p(d-1)\leq(p-1)(E_p+1)$. In the remaining case $k=p$, the valuation is zero if $p\nmid i$; if $i=ph$, extracting $p$ loses at most one further unit. Both small primes therefore satisfy $v_p(T(n))\geq e-E_p-2$. The factor $L_{12R}$ supplies $E_p$, $36=2^23^2$ supplies the small-prime allowance, and $(R-1)!$ handles the other factors.

For the second family, every factor is coprime to six. If $p^j>R$ divides $12n-i$, the fractional residue is $q/12+i/(12p^j)$, $q\in\{1,5,7,11\}$, in a right-hand cell with $G=1$. Hence $v_p(T(n))\geq e-\lfloor\log_pR\rfloor$, supplied by $L_R$ and the same product bound. Finally, $12n-i=0$ contradicts $\gcd(i,12)=1$, so no denominator vanishes.
:::


::: {.corollary #cor-6 title="Coefficient formulas and growth" status="written-proof" proof="pf-6" doi="10.5281/zenodo.23971279" source="Corollary 6" request="https://github.com/the-omega-institute/trureturing-requests/issues/267" mathesis="collected:bala295462:4:s6"}
The binomial identities, hypergeometric series and asymptotic formulas in A295462 and A295431 hold, as does Mathar's recurrence for A295431. The proof below explicitly lists the formulas and definitions meant by source §6, Corollary 6.
:::


::: {.proof #pf-6}

Source §6, Corollary 6. Expanding factorials gives Chai Wah Wu's two A295462 identities:


$$
a(n)=\frac{\binom{15n}{5n}\binom{2n}{n}}{\binom{6n}{n}},
$$


$$
a(n)=\frac{\binom{15n}{5n}\binom{7n}{n}}{\binom{7n}{2n}}.
$$

Divide every element of the first displayed set by $15$, and define the parameters:


$$
\begin{aligned}A&=\{1,2,4,7,8,11,13,14\}/15,\\B=\{&1/10,1/6,3/10,1/2,\\&7/10,5/6,9/10\},\\C&=61509375/16384.\end{aligned}
$$


$$
\frac{a(n+1)}{a(n)}=\frac{C\prod_{\alpha\in A}(n+\alpha)}{(n+1)\prod_{\beta\in B}(n+\beta)}.
$$

This ratio follows by cancellation of consecutive factorials, with $C=15^{15}2^2/(10^{10}6^6)$. Define the rising factorial by $(q)_0=1$ and $(q)_n=q(q+1)\cdots(q+n-1)$. The $n$th term of ${}_pF_q(A;B;z)$ is $\prod_{\alpha\in A}(\alpha)_n\,z^n/(n!\prod_{\beta\in B}(\beta)_n)$. The initial value $a(0)=1$ and this ratio uniquely determine the coefficients, so as a formal power series,


$$
\sum_{n\geq0}a(n)z^n={}_8F_7(A;B;Cz).
$$

Stirling's formula gives the asymptotic expression recorded by Amiram Eldar in A295462:


$$
a(n)\sim\frac1{2\sqrt{\pi n}}\left(\frac{3^95^5}{2^{14}}\right)^n\quad(n\to\infty).
$$

The factors $e^{-kn}$ cancel, the powers of $n$ leave $n^{-1/2}$, and the square-root constant is $\sqrt{30/60}/\sqrt{2\pi n}=1/(2\sqrt{\pi n})$.

For $T(n)$ the same cancellation gives Wu's two A295431 identities:


$$
T(n)=\frac{\binom{12n}{6n}\binom{6n}{2n}}{\binom{3n}{n}},
$$


$$
T(n)=\frac{\binom{12n}{6n}\binom{7n}{3n}}{\binom{7n}{n}}.
$$

The consecutive ratio is Mathar's recurrence ($n\geq1$):


$$
\begin{aligned}\frac{T(n)}{T(n-1)}={}&\frac{24(12n-11)(12n-1)}{n(3n-1)}\\&\cdot\frac{(12n-5)(12n-7)}{(2n-1)(3n-2)}.\end{aligned}
$$

Using $T(0)=1$ and the same coefficient-ratio argument gives the formal generating function, with its parameters on separate lines:


$$
\begin{aligned}A_T&=(1/12,5/12,7/12,11/12),\\B_T&=(1/3,1/2,2/3).\end{aligned}
$$


$$
\sum_{n\geq0}T(n)z^n={}_4F_3(A_T;B_T;27648z).
$$

Finally, Penson's expansion is (as $n\to\infty$)


$$
\begin{aligned}T(n)=\frac{27648^n}{\sqrt{12\pi n}}\bigg(&1+\frac1{36n}\\&+\frac1{2592n^2}+O(n^{-3})\bigg).\end{aligned}
$$

Stirling's logarithmic expansion gives the square-root prefactor $1/\sqrt{12\pi n}$ and the $1/n$ coefficient $(1/12+1-1/6-1/4-1/3)/12=1/36$. There is no $1/n^2$ term in the logarithm; exponentiating supplies $1/(2\cdot36^2)=1/2592$, with the Stirling remainder giving $O(n^{-3})$. The formal series identities require no choice of a convergence point. The asymptotics apply along positive integers as $n\to\infty$, and are not evaluated at $n=0$.

:::
