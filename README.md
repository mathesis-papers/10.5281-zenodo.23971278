# Parity and product extensions of Bala's divisibilities (2026): OEIS A295462, References (record #19; contribution dated 23 August 2026)

**Authors:** Haobo Ma, Wenlin Zhang

Extending Bala's divisibility results (Bala, 2026), we prove his conjecture in OEIS A295462, References (%D), record #19; contribution dated 23 August 2026: the integer a(n)=(15n)!(2n)!/((10n)!(6n)!n!) is odd exactly when consecutive one-bits of n have at least three zero-bits between them. A nonnegative floor function expresses its prime valuations. We reprove Bala's two divisibilities (Bala, 2026) and deduce product divisibility by (6n+1)(10n+1), preservation of the parity criterion, and counting and ordered recursions. We give written alternative proofs of the eleven XOR identities in A048718, verified by Karlsson (2022) with Walnut. For T(n)=(12n)!n!/((6n)!(4n)!(3n)!), we prove the five fixed divisibilities and both product families posed in A295431 on 28 August 2025, with C(k,R)=36(R-1)!lcm(1,...,12R) for k=1,2,3 and D(R)=(R-1)!lcm(1,...,R).

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23971279](https://doi.org/10.5281/zenodo.23971279)
- Concept DOI: [https://doi.org/10.5281/zenodo.23971278](https://doi.org/10.5281/zenodo.23971278)
- License: CC-BY-4.0
- Version: 4
- Mathesis record: [bala295462](https://mathesis-omega-research.apps.chrono-ai.fun/papers/bala295462?version=4)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Parity and product extensions of Bala's divisibilities (2026): OEIS A295462, References (record #19; contribution dated 23 August 2026). Mathesis, version 4. https://doi.org/10.5281/zenodo.23971279

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |
| Corollary (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23971278/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23971278/bala295462/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23971278/bala295462/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23971278/bala295462/slides/) ([sources](books/bala295462/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23971278/bala295462/films/) ([sources](books/bala295462/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23971278/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `thm-parity` | same | `D5/S3/Arith/FactorialRatio/BalaA295462Parity.result` |
| `cor-2` | variant | `D5/S3/Arith/FactorialRatio/BalaA295462Parity.result` |
| `cor-3` | variant | `D5/S3/Arith/FactorialRatio/BalaA295462Parity.result` |
| `cor-4` | variant | `D5/S3/Arith/FactorialRatio/BalaA295462Parity.result` |
| `cor-families` | same | `D5/S3/Arith/FactorialRatio/BalaA295431Divisibility.result` |
| `cor-6` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/bala295462/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
