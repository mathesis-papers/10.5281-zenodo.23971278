# Parity and product extensions of Bala's divisibilities (2026): OEIS A295462, References (record #19; contribution dated 23 August 2026)

Revision 4 — 4 November 2026.

The posing locator is Peter Bala's 23 August 2026 contribution in OEIS
A295462, References (%D), record #19: https://oeis.org/A295462/internal.
The note proves integrality of `(15n)!(2n)!/((10n)!(6n)!n!)` and its
oddness exactly at the indices whose occupied binary positions are at least
four apart, including zero. Division by `(6n+1)(10n+1)` preserves this criterion.

## Mathematical coverage

- Theorem 1: the complete integrality and parity equivalence.
- Corollary 2: reproofs of Bala's two divisibilities (2026), with their product
  and its parity consequence.
- Corollary 3: counting and ordered enumeration of the odd indices.
- Corollary 4: written alternative proofs of the eleven Hanna XOR identities
  in A048718, verified by Karlsson (2022) with Walnut, and the general
  disjoint-block rule for bounded masks.
- Corollary 5: the five fixed A295431 divisibilities and both product families,
  with `C(k,R)=36(R-1)!lcm(1,...,12R)` for `k=1,2,3` and
  `D(R)=(R-1)!lcm(1,...,R)`.
- Corollary 6: the two entries' binomial, generating-function and asymptotic
  formulas, and the A295431 recurrence.

The two factorial ratios' integrality is reproved; the prior proof is Bober
(2007 preprint, 2009 publication), whose sporadic classification is cited
rather than reproved. Soundararajan (2019) gives a later elementary proof
of that classification. A295462 is row 32 in Bober's table; A295431 is a
different ratio, whose linked parameter list includes that row.

The pinned Lean declaration
`D5.S3.Arith.FactorialRatio.BalaA295462Parity.result` proves the exact rational
quotient's natural realization and its parity equivalence in Theorem 1:
https://github.com/the-omega-institute/trureturing/blob/b95cdbb8cccca425964251ba38cc0b0e517e478a/D5/S3/Arith/FactorialRatio/BalaA295462Parity.lean.
The corollaries have written proofs. The source-coverage table credits
Zudilin's prime-step congruence (2019), Bajaj and Burns' general tower theorem
(August 2026), and Blanco Gomez's later explicit tower treatment (October 2026).
Blanco Gomez also proves the Gamma-factorial integrality statements.
The corresponding half/third questions were already posed by Bala (2016, p. 5).
The table separates the remaining moment-density and other-ratio statements.

## Build and check

The package uses Python 3's standard library and Tectonic 0.17.0:

```sh
python3 verify.py > verification.new.json
cmp verification.json verification.new.json
tectonic note.tex
```

Alternatively run `pdflatex note.tex` twice. The bibliography is embedded in
`note.tex`; no BibTeX step or additional input file is required.
`manifest.sha256` identifies every scientific source member:

```sh
sha256sum -c manifest.sha256
```

The finite checks use exact integers and rational arithmetic: all 30 cells
for F and all 12 for G; parity for `0<=n<65536`; direct factorial and
divisibility identities through 256; all eleven XOR identities on the 250
sparse indices below 65536; all 256 pairs of four-bit masks; both product
families for `n=0..256`, `R=1..32`, `k=1,2,3`; 44352 constructed small-prime
cases with exponents up to 96; and coefficient/counting identities.
These finite ranges complement the all-input written proofs.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0: https://creativecommons.org/licenses/by/4.0/.
