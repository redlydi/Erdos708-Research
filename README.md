Erdős–Surányi Problem #708 — Research Project

Independent mathematical research on Erdős Problem #708, focusing on number theory, combinatorics, prime-power coverings, probabilistic methods, and computational verification.

Research status: Active. Several partial asymptotic results have been developed. The universal conjecture remains open, and the new proofs require independent verification.

1. Main research objective

Let (A\subseteq{2,\ldots,M}) consist of (n) distinct integers, where (M=\max A). Let (I) be an interval of (M) consecutive integers.

Define (\tau(A,I)) as the minimum size of a subset (B\subseteq I) satisfying

[
\prod_{a\in A}a\mid\prod_{b\in B}b.
]

Let (g(n)) be the maximum possible value of (\tau(A,I)) over all admissible (A) and (I).

Our main objective is to establish

[
\boxed{g(n)\le(2+o(1))n.}
]

This universal asymptotic bound has not been proved by this project.

2. Main research results

The following statements are presented with mathematical arguments in the linked reports. They are research claims pending independent mathematical verification, not externally certified theorems.

Research direction| Reported result| Scope
Large intervals| (H(A,I)\le2n+o(n))| (M\ge n^{3/2+\varepsilon}), every shift
Dense intervals| (H(A,I)\le2n)| (M\le(2+c)n), every shift, some absolute (c>0)
Polynomially bounded shifts| (H(A,I)\le2n+o(n))| (M\ge n^{1+\varepsilon}), (x+M\le M^K)
Almost-all-shift theorem| (H(A,I)\le2n+o(n))| Almost all shifts in sufficiently long ranges
Arithmetic shift certificates| (H(A,I)\le2n+o(n))| Certain arbitrarily large shifts satisfying polynomial congruences
Weighted stability| (Q(A,I)\le Q(B,I)+O(m\log(eM/m)))| Dense case, (m=

Here (H(A,I)) denotes the minimum number of interval points covering the required multiplicities of every prime-power level, so that

[
\tau(A,I)\le H(A,I).
]

The weighted functional (Q) is studied through linear-programming duality, with the reported reduction

[
Q(A,I)\le\tau(A,I)\le Q(A,I)+s,
]

where (s) is the number of distinct prime divisors appearing in (A).

The conclusions above are conditional on the correctness of their respective proofs. Computational tests do not establish the general statements.

3. Key research reports

Latest asymptotic investigations

- "Prime-power-level covering" (reports/erdos708-power-level-cover%20%281%29.md) — Unitary factorization, collision estimates, and the proposed large-(M) theorem.

- "Density and shifts" (reports/erdos708-density-and-shifts%282%29.md) — Near-saturated prime-power progressions, a proposed density breakthrough beyond (M=2n), and deterministic control of polynomially bounded shifts.

- "Residue certificates and weighted stability" (reports/erdos708-residue-certificates.md) — Polynomial congruence certificates for large shifts, stability of weighted optima, and limitations of two-level fractional coverings.

Earlier structural investigations

- "Interval transport" (reports/erdos708-interval-transport%20%281%29.md) — Transport of divisibility requirements across intervals.
- "Group deficit and repair" (reports/group-deficit-and-repair.md) — Collision deficits, composite-divisor repair, and limitations of independent representative selection.
- "Bounded prime factors" (reports/bounded-prime-factors.md) — Structural bounds under restrictions on prime factors.
- "Growing prime factors" (reports/growing-prime-factors.md) — Extensions to families with growing factorization complexity.
- "Main research archive" (reports/REPORT.md) — Earlier research results, arguments, computations, and open questions.

Additional investigations are available in the ""reports/"" (reports/) directory.

4. Remaining open problems

The central unresolved objective is to prove

[
H(A,I)\le2n+o(n)
]

or directly

[
\tau(A,I)\le2n+o(n)
]

uniformly for all admissible families and all interval shifts.

Important obstacles include:

1. Intermediate interval lengths: the region between the established candidate regimes for dense and very large intervals.
2. Worst-case shifts: arbitrary, potentially enormous shifts with unusually concentrated divisibility patterns.
3. Joint prime-factor collisions: controlling the actual cost of overlapping requirements rather than overcounting pairwise conflicts.
4. Weighted covering: obtaining uniform bounds for the LP-dual functional (Q(A,I)).
5. Overloaded interval points: proving that removing points with anomalously large divisor loads leaves only a negligible number of uncovered source requirements.

A promising direction is to combine unitary block methods, weighted compensation, and stability under exceptional source elements.

No complete resolution of these obstacles is claimed.

5. Repository structure

Erdos708-Research/
├── README.md
├── reports/
│   ├── REPORT.md
│   ├── erdos708-power-level-cover (1).md
│   ├── erdos708-density-and-shifts(2).md
│   ├── erdos708-residue-certificates.md
│   └── ...
├── code/
│   ├── check.py
│   ├── archive_g3.py
│   └── archive_repetitions.py
└── verification/
    ├── check_output.txt
    ├── archive_g3_output.txt
    └── archive_repetitions_output.txt

6. Computational verification

The repository includes Python experiments and recorded outputs.

Run from the repository root:

python3 code/check.py
python3 code/archive_g3.py
python3 code/archive_repetitions.py

The latest asymptotic reports also contain self-contained Python verification snippets.

These computations test finite cases or auxiliary identities. They are not exhaustive proofs of the asymptotic results.

Verification policy

We distinguish between:

- Mathematically proved statements: results supported by complete arguments and subsequently checked.
- Computationally verified statements: claims verified within specified finite ranges.
- Research claims pending verification: proposed theorems supported by written arguments but not yet independently certified.
- Conjectures and open problems: statements for which no complete proof is currently available.

The newest asymptotic theorems belong to the third category pending further review.

No Lean verification of these latest asymptotic results is claimed. Independent verification, counterexample searches, and comparison with existing mathematical literature remain necessary.

7. Related research

Our project investigates approaches related to those explored in:

"DenisUkranian/erdos-708-research" (https://github.com/DenisUkranian/erdos-708-research)

Potential connections include weighted covering estimates, two-block certificates, computational methods, and exceptional divisibility configurations.

This reference does not imply that either research program has proved the universal asymptotic conjecture.

8. References

- "Erdős Problems — Problem #708" (https://www.erdosproblems.com/708)
- "Related research by DenisUkranian" (https://github.com/DenisUkranian/erdos-708-research)

---

Project status (November 2026): Active independent research. Partial asymptotic results proposed; independent verification pending. The universal bound (g(n)\le(2+o(1))n) remains an open objective.
