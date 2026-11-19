# Sources and contributions

This explanation, presentation and film follow version 4 of the paper by Haobo Ma and Wenlin Zhang. Haobo Ma is affiliated with Chrono AI, Singapore; Wenlin Zhang with Chrono AI and the National University of Singapore, Singapore. Names retain their source spelling.

## The paper and earlier work

Bober's classification already established integrality of the two factorial ratios here. Bala (2026) proved divisibility by $6n+1$ and $10n+1$. This paper proves the binary-spacing parity characterization, derives quotient and enumeration consequences, gives alternative written proofs of Hanna's eleven identities, and handles the fixed divisibilities and both A295431 product families. Karlsson's Walnut verification precedes these alternative proofs.

The A295431 prime-power congruences have prior proofs. Bajaj–Burns (August 2026), followed by Blanco Gómez (October 2026), give

$$
T(np^k)\equiv T(np^{k-1})\pmod{p^{3k}}
$$

for primes $p\geq5$ and $n,k\geq1$, through the classical Jacobsthal–Kazandzidis binomial congruence cited by the source. Zudilin covers the one-level case $k=1$. Integrality of $T(n/2)$ and $T(n/3)$ in the Gamma-factorial interpretation is Blanco Gómez's Corollary 1.5; the questions already occur in Bala (2016), p. 5. These results are distinct from the product divisibilities in [@cor-families].

## References

- Haobo Ma and Wenlin Zhang, *Parity and product extensions of Bala's divisibilities (2026): OEIS A295462, References (record #19; contribution dated 23 August 2026)*, version 4. [DOI:10.5281/zenodo.23971279](https://doi.org/10.5281/zenodo.23971279). CC BY 4.0. [Original PDF](https://zenodo.org/api/records/23971279/files/note-v4.pdf/content).
- OEIS Foundation, [A295462, internal record #19](https://oeis.org/A295462/internal). Entry by Gheorghe Coserea (28 November 2017); References contribution by Peter Bala (23 August 2026).
- Peter Bala, *A295462(n) is divisible by 6*n+1 and 10*n+1*, 23 August 2026, [three-page note](https://oeis.org/A295462/a295462.pdf).
- Jonathan W. Bober, *Factorial ratios, hypergeometric series, and a family of step functions*, J. London Math. Soc. (2) **79** (2009), 422–444. [DOI:10.1112/jlms/jdn078](https://doi.org/10.1112/jlms/jdn078). [arXiv:0709.1977v1](https://arxiv.org/abs/0709.1977v1), Theorem 3.1, Lemma 3.2, Table 2 row 32.
- K. Soundararajan, *Integral factorial ratios*, [arXiv:1901.05133v1](https://arxiv.org/abs/1901.05133v1), 16 January 2019, Theorem 1.1 and proof.
- OEIS Foundation, [A048718, internal record #25](https://oeis.org/A048718/internal). Entry by Antti Karttunen (30 March 1999); Comments and Formula fields include Hanna's eleven identities (22 January 2006).
- Sebastian Karlsson, *Walnut code that verifies the conjectures of Paul D. Hanna*, 31 December 2022, [public formulas](https://oeis.org/A048718/a048718.txt).
- OEIS Foundation, [A295431, internal record #101](https://oeis.org/A295431/internal). Entry by Gheorghe Coserea (22 November 2017); Bala's divisibility questions in Comments (28 August 2025). Formula attributions to Chai Wah Wu, Mathar and Penson are retained as recorded in the source paper.
- Wadim Zudilin, *Congruences for q-binomial coefficients*, [arXiv:1901.07843v2](https://arxiv.org/abs/1901.07843v2), 1 April 2019, §5, Theorem 3.
- Ravi Bajaj and Alexander Burns, *Balanced factorial ratios inherit a cubic tower*, August 2026, §1, [pinned scientific text](https://github.com/rbajaj5/a183068-supercongruence/blob/d819eb8e8e70fdd386978adc4cbbdb2033466d40/related-results/BalancedFactorialRatioCubicTowers.md).
- Peter Bala, *Some integer ratios of factorials*, August 2016, [six-page note](https://oeis.org/A276098/a276098.pdf), p. 5.
- Roberto Blanco Gómez, *Supercongruences modulo $p^{3k}$ and integrality for factorial ratios with fractional arguments, with proofs of conjectures of P. Bala*, 17 October 2026. [DOI:10.5281/zenodo.23426707](https://doi.org/10.5281/zenodo.23426707), Corollaries 1.4(d), 1.5, proofs in §5.2.

## Contribute a formalization

Four written results still need their matching formalization; each already has a manuscript proof:

- [Removing two odd factors](https://github.com/the-omega-institute/trureturing-requests/issues/264): reuse the parity theorem and establish quotient integrality and parity.
- [Counting and ordered enumeration](https://github.com/the-omega-institute/trureturing-requests/issues/265): reuse spacing and handle short words and recurrence boundaries.
- [Bitwise operations and eleven identities](https://github.com/the-omega-institute/trureturing-requests/issues/266): four-bit block formulas plus the two extra one-step-carry arguments.
- [Coefficient formulas and asymptotics](https://github.com/the-omega-institute/trureturing-requests/issues/267): exact coefficient ratios, formal series and Stirling expansions.

Coordinate scope on the corresponding request, work on a focused branch in your own fork, and submit directly to upstream `dev` under its [contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). A shared request records work; it does not certify a proof. Original authors, earlier work and formalization contributions receive separate attribution. The existing parity theorem and A295431 divisibilities need no duplicate construction.
