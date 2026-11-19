# Three zeros decide parity

Write $17$ in binary: $10001$. There are exactly three zeros between its two ones. Write $9$ in binary: $1001$. There are only two. That single missing zero decides the parity of a huge factorial quotient.

The factorial $m!$ is the product from $1$ to $m$, with $0!=1$. The paper studies

$$
a(n)=\frac{(15n)!(2n)!}{(10n)!(6n)!n!},\qquad n\geq0.
$$

Haobo Ma and Wenlin Zhang prove: **this quotient is always a positive integer, and it is odd exactly when consecutive ones in the binary expansion of $n$ have at least three zeros between them.** A single one satisfies the condition. So does $0$, whose binary support is empty; indeed $a(0)=1$. See [@thm-parity] for the precise statement; positivity follows directly from positivity of the factorials.

For example, $a(1)=1001=7\cdot11\cdot13$ is odd. The rule says that $a(9)$ is even and $a(17)$ is odd without expanding $135!$ or $255!$. This is the benefit: a question about enormous products becomes a question about the digits of the input.

Peter Bala posed this parity conjecture in the References field of OEIS A295462 on 23 August 2026, and proved the two divisibilities discussed below. Gheorghe Coserea entered the sequence in 2017. This explanation follows [version 4 of the paper](https://doi.org/10.5281/zenodo.23971279). Integrality of these factorial ratios was already part of Jonathan W. Bober's earlier classification.

## Count the factors of two

A positive integer is even if it contains at least one factor of $2$. For example, $12=2^2\cdot3$ contains two. Write $v_p(N)$ for the number of factors of a prime $p$ in a positive integer $N$. For a positive rational number, subtract the denominator's count from the numerator's.

In $m!$, each even number contributes one factor of $2$, each multiple of $4$ contributes another, and each multiple of $8$ another. Thus

$$
v_2(m!)=\left\lfloor\frac m2\right\rfloor
+\left\lfloor\frac m4\right\rfloor+\cdots.
$$

Here $\lfloor x\rfloor$ is the greatest integer at most $x$. Apply the same count to any prime $p$, and subtract the denominator counts in the factorial quotient:

$$
v_p(a(n))=\sum_{k\geq1}F(n/p^k),
$$

where the longer expression is easier to read on two lines:

$$
\begin{aligned}
F(x)={}&\lfloor15x\rfloor+\lfloor2x\rfloor\\
&-\lfloor10x\rfloor-\lfloor6x\rfloor-\lfloor x\rfloor.
\end{aligned}
$$

The sum is finite: every term vanishes once $p^k>15n$. Because $15+2=10+6+1$, adding $1$ to $x$ leaves $F(x)$ unchanged. We only need $0\leq x<1$, and all jumps lie on a grid of spacing $1/30$. Checking its thirty cells shows that $F$ takes only the values $0$ and $1$.

No prime can remain in the reduced denominator, so $a(n)$ is an integer. More decisively, the summands cannot cancel: $a(n)$ is odd exactly when every $F(n/2^k)$ is zero.

## Why three zeros?

Binary position $e$ has weight $2^e$. If the ones are at least four positions apart, the tail $R$ below an occupied position $e$ can occupy, at most, positions $e-4,e-8,\ldots$. Hence

$$
\begin{aligned}0\leq R&<2^e\left(\frac1{16}+\frac1{16^2}+\cdots\right)\\&=\frac{2^e}{15}.\end{aligned}
$$

The inequality is strict because an integer has finitely many digits. The denominator $15$ comes from the geometric sum $1/16+1/16^2+\cdots=1/15$: it links the four-position spacing to the factorial coefficients.

Dividing by $2^k$ and taking the fractional part reads just the last $k$ binary digits. If their highest occupied position is $t$, this fraction is $(1+u)/2^\ell$, where $\ell=k-t\geq1$ and $0\leq u<1/15$. Checking $\ell=1,2,3$, and then $\ell\geq4$, gives $F=0$ in every case. Sufficient spacing leaves no factor of two.

Conversely, move from low positions to high positions and find the first pair $e<t$ less than four positions apart. Its distance is $d=1,2,3$. The lower digits have not yet violated the rule, so the same tail bound applies. Reading the last $t+1$ digits gives

$$
x=\frac{2^d+1+u}{2^{d+1}},\qquad 0\leq u<1/15.
$$

All three cases give $F(x)=1$. That single summand is enough: all others are nonnegative, so the quotient is even. The [precise proof](statements.md#pf-parity) includes the small tables that make both checks explicit.

The film connects these steps: read a suffix, inspect its gap, and detect the surviving factor of two.

::: {.film src="001-binary-spacing"}
Three zeros decide parity: from $9$ and $17$ to nonnegative prime-factor counts.
:::

## Beyond odd and even

Bala proved that both $6n+1$ and $10n+1$ divide $a(n)$. Both are odd, and any common divisor divides

$$
5(6n+1)-3(10n+1)=2.
$$

They are therefore coprime, so their product also divides $a(n)$. Dividing by this odd product preserves parity. This is [@cor-2]; at $n=1$, for example, $1001/(7\cdot11)=13$.

The spacing rule also counts. Let $c_m$ count inputs $0\leq n<2^m$ with odd $a(n)$. Write them as $m$-digit binary words, allowing leading zeros. For $m\geq4$, a valid word begins either with $0$ or with $1000$, giving

$$
\begin{aligned}
c_0=1,\quad c_1=2,\quad c_2=3,\quad c_3=4,\\
c_m=c_{m-1}+c_{m-4}\qquad(m\geq4).
\end{aligned}
$$

Thus $c_4=5$ and $c_5=7$. The valid inputs below $32$ are $0,1,2,4,8,16,17$. [@cor-3] also gives a recursion that lists all valid inputs in increasing order.

Another application concerns bitwise operations. XOR returns one when the two bits differ; AND returns one when both are one; OR returns one when at least one is one. If the ones in $n$ are at least four positions apart and $u<16$, multiplying by $u$ places copies of its four-bit pattern in disjoint windows. Consequently, for $0\leq u,v<16$,

$$
(un)\oplus(vn)=(u\oplus v)n.
$$

The analogous statements hold for AND and OR. For $n=17$, $u=3$, $v=9$, each window works independently: $51\oplus153=170=10\cdot17$. The paper also handles two identities outside the four-bit mask range using carries that stop after one position; [@cor-4] preserves them. Paul D. Hanna listed the eleven XOR identities in 2006; Sebastian Karlsson verified them with Walnut in 2022. This paper gives alternative written proofs using binary support.

## A second factorial quotient

OEIS A295431 concerns a different number:

$$
T(n)=\frac{(12n)!n!}{(6n)!(4n)!(3n)!}.
$$

It must be distinguished from $a(n)$. It has its own periodic floor function taking values zero and one. The paper uses it to answer five divisibility questions posed by Bala on 28 August 2025, and to handle two product families of arbitrary length. For example,

$$
\frac{770T(n)}{(n+1)(2n+1)(3n+1)}\in\mathbb Z.
$$

There are exactly three factors in that denominator. More generally, after fixing a length $R\geq1$, one can choose a constant independent of $n$ that makes division by $\prod_{i=1}^R(kn+i)$ integral for $k=1,2,3$. The other family uses factors $12n-i$ with $i$ coprime to $12$. These factors may be negative but never zero. [@cor-families] gives the constants and all boundary cases.

Why can one constant handle a whole product? For each prime, select the denominator factor containing it to the highest power. Every other factor differs from this one by a difference of indices. The product of those differences is controlled by $(R-1)!$. The strongest factor is controlled by the floor function for $T(n)$ and a least common multiple. An arbitrary product reduces to one factor plus its index differences. The constants are sufficient; the paper does not assert that they are smallest.

## Evidence and limits

The [precise statements and proofs](statements.md) retain all six source results, including both sets of binomial formulas, the hypergeometric generating functions, Mathar's recurrence, and the asymptotic expansions. Numerical examples in the story illustrate the argument; they do not replace proofs for all inputs.

The [Lean parity declaration](lean:D5/S3/Arith/FactorialRatio/BalaA295462Parity.result) proves that a natural number realizes the rational quotient and characterizes its parity. Positivity follows from the positive factorials. The [Lean divisibility declaration](lean:D5/S3/Arith/FactorialRatio/BalaA295431Divisibility.result) covers all five fixed A295431 divisibilities and both unbounded product families. The quotient $b(n)$, counting, bitwise operations and additional formulas retain written proofs and their shared formalization requests here.

These results do not supply A295431's explicit moment density, its shape or uniqueness, or analogous divisibility results for each of the other 51 sporadic ratios. Prime-power congruences and integrality at half and third arguments have prior proofs cited by the manuscript; they are distinct from the two product families here. See [Sources](sources.md) for attribution and contribution links.

The seminar follows the same path from examples to the mechanism and its extensions.

::: {.slides src="seminar"}
An academic presentation with aligned Chinese and English frames and speaker notes.
:::
