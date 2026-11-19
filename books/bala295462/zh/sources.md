# 文献与贡献

本解读、报告与视频源于 Haobo Ma、Wenlin Zhang 的第 4 版论文。Haobo Ma 的机构为 Chrono AI（Singapore）；Wenlin Zhang 的机构为 Chrono AI 与 National University of Singapore（Singapore）。作者姓名保留原文写法。

## 原文与前人工作

Bober 的分类已给出这里两个阶乘商的整性。Bala（2026）已证明 $6n+1$、$10n+1$ 的整除性。本文证明二进制间距的奇偶刻画，推导商与递推，给出 Hanna 十一条恒等式的书面替代证明，并处理 A295431 的固定整除性与两个乘积族。Karlsson 的 Walnut 验证早于这里的替代证明。

A295431 的素数幂同余有既有证明：Bajaj–Burns（2026 年 8 月）及随后 Blanco Gómez（2026 年 10 月）的结果给出

$$
T(np^k)\equiv T(np^{k-1})\pmod{p^{3k}}
$$

其中 $p\geq5$ 是素数，$n,k\geq1$；原文归于经典 Jacobsthal–Kazandzidis 二项式同余，Zudilin 的结果覆盖一个层级 $k=1$。Gamma 阶乘意义下 $T(n/2)$ 与 $T(n/3)$ 的整性见 Blanco Gómez 的 Corollary 1.5；问题早已见于 Bala（2016），p. 5。这些结果与 [@cor-families] 的乘积整除性不同。

## 文献

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

## 参与形式化

本书有四项书面结果待补齐对应形式化，均已有原文证明：

- [除去两个奇因子](https://github.com/the-omega-institute/trureturing-requests/issues/264)：复用奇偶定理，补商的整性与奇偶性。
- [计数与按序生成](https://github.com/the-omega-institute/trureturing-requests/issues/265)：复用间距刻画，处理短串与递推边界。
- [位运算与十一条恒等式](https://github.com/the-omega-institute/trureturing-requests/issues/266)：四位块公式及两个额外的一步进位论证。
- [系数公式与渐近式](https://github.com/the-omega-institute/trureturing-requests/issues/267)：精确系数比、形式级数与 Stirling 展开。

先在对应请求中协调范围，再在贡献者自己的 fork 中作聚焦分支，按[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)直接向 `dev` 提交 PR。共享请求记录工作，不替代证明；原作者、前人工作与形式化贡献分别署名。已有的奇偶定理及 A295431 整除性无需重复构造。
