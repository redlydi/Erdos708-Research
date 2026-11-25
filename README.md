# Erdős–Surányi Problem 708

Independent research on Erdős Problem #708,
focusing on number theory, combinatorics,
structural bounds and computational verification.

## Research objective

Establish the asymptotic upper bound:

**g(n) ≤ (2 + o(1))n**

This remains an open research objective.

## Research directions

- Prime-power support inclusion and antichains.
- Bounds for bounded composite cores.
- Pairwise coprime core structures.
- Hall-type matching arguments.
- Repeated prime factors.
- G2 and G3 special cases.
- Structural reductions involving four distinct primes.

## Main results under investigation

| Result | Status |
|---|---|
| Prime-power support bound | Requires independent verification |
| 2n + C(k) bound | Requires independent verification |
| 2n − 1 + f bound | Requires independent verification |
| G3 stability | Computational and theoretical investigation |
| General asymptotic bound | Open |

## Repository structure

| Directory | Description |
|---|---|
| [reports](reports/) | Mathematical research and proofs |
| [code](code/) | Python verification scripts |
| [verification](verification/) | Computational outputs |

## Research report

Read the [full research report](reports/REPORT.md)
for mathematical arguments, constructions,
experimental results and open questions.

## Reproducing computations

Run from the repository root:

    python3 code/check.py
    python3 code/archive_g3.py
    python3 code/archive_repetitions.py

Recorded outputs are available in `verification/`.

## Verification policy

Computational experiments do not constitute
proofs of general mathematical statements.

New theoretical results require independent
mathematical verification.

## References

- [Erdős Problem #708](https://www.erdosproblems.com/708)

## Project status

Active mathematical research.
