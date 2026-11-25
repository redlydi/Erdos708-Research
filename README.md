# Erdős–Surányi Problem #708

### Independent research in number theory and combinatorics

Research repository dedicated to [Erdős Problem #708](https://www.erdosproblems.com/708), focusing on asymptotic bounds, prime-power coverings, combinatorial methods, and computational verification.

> **Research status — November 2026**
>
> Several partial asymptotic results have been proposed. The universal coefficient $2$ remains unproved. New written arguments have not yet undergone independent mathematical or formal verification.

---

## 1. Main Problem

Let $A=\{a_1,\ldots,a_n\}\subseteq\{2,\ldots,M\}$ consist of $n$ distinct integers, where $M=\max A$. Let $I$ be an interval of $M$ consecutive positive integers.

A subset $B\subseteq I$ is **admissible** when

$$
\prod_{a\in A} a \mid \prod_{b\in B} b.
$$

Define $\tau(A,I)$ as the minimum size $|B|$ of an admissible subset, and set

$$
g(n)=\sup_{A,I}\tau(A,I).
$$

### Main research objective

Establish the universal asymptotic bound

$$
\boxed{g(n)\le (2+o(1))n.}
$$

**This is an open research objective, not a result established by this repository.**

---

## 2. Prime-Power Covering Framework

For an integer $q\ge2$ and a finite set $X$, define



A subset $B\subseteq I$ is a **prime-power cover** of $A$ when

$$
C_B(p^j)\ge C_A(p^j)
$$

for every prime power $p^j\le M$.

Let $H(A,I)$ be the minimum size of a prime-power cover. Covering all prime-power levels implies product divisibility, hence

$$
\boxed{\tau(A,I)\le H(A,I).}
$$

A major research goal is to prove $H(A,I)\le2n+o(n)$ uniformly over all admissible $A$ and all shifts of $I$.

---

## 3. Main Research Results

The results below are **claims supported by written research reports**. They are not represented as externally verified theorems. All asymptotic statements refer to $n\to\infty$ with fixed auxiliary parameters.

### 3.1. Large-$M$ asymptotic covering

For each fixed $\varepsilon>0$, the project proposes that some $c_\varepsilon>0$ satisfies

$$
M\ge n^{3/2+\varepsilon}
\quad\L$$
C_X(q)=\#\{a\in X:q\mid a\}.
$$

ongrightarrow\quad
H(A,I)\le2n+O_\varepsilon(n^{1-c_\varepsilon})
$$

uniformly over all families and interval shifts.

**Methods:** unitary decomposition of prime-power atoms, greedy divisor extraction, random injections, gcd-sum collision estimates, and repair of deficient levels.

**Report:** [Prime-power-level covering](reports/erdos708-power-level-cover%20%281%29.md)

### 3.2. Dense-interval bound

A separate argument proposes the existence of an absolute constant $c>0$ such that, for sufficiently large $n$,

$$
M\le(2+c)n
\quad\Longrightarrow\quad
H(A,I)\le2n
$$

for every shift.

**Methods:** near-saturated prime-power progressions, moment estimates, fractional coverings, and rounding. The argument does not provide an explicit numerical value of $c$.

**Report:** [Density and shifts](reports/erdos708-density-and-shifts%282%29.md)

### 3.3. Polynomially bounded shifts

For fixed $\varepsilon>0$ and $K\ge1$, with $I=(x,x+M]$, a proposed intermediate-range result assumes

$$
M\ge n^{1+\varepsilon},\qquad x+M\le M^K
$$

and concludes that, for some $\eta>0$,

$$
H(A,I)\le2n+O_{\varepsilon,K}(n^{1-\eta}).
$$

This does not handle arbitrary shifts.

**Report:** [Density and shifts](reports/erdos708-density-and-shifts%282%29.md)

### 3.4. Arithmetic certificates for large shifts

Define

$$
L_M=\mathrm{lcm}(1,2,\ldots,M).
$$

The latest investigation studies shifts $x$ for which a nonzero polynomial $F\in\mathbb{Z}[X]$ of bounded degree and polynomially bounded coefficients satisfies

$$
F(x)\equiv0\pmod{L_M}.
$$

Under the conditions specified in the report, the proposed result is

$$
H(A,I)\le2n+O(n^{1-\eta})
$$

for some $\eta>0$. These certificates apply to certain astronomically large shifts, but not every residue class.

**Report:** [Residue certificates and weighted stability](reports/erdos708-residue-certificates.md)

### 3.5. Weighted covering and stability

For weights $0\le w_p\le1$, put

$$
X_w(a)=\sum_p w_p v_p(a).
$$

The weighted dual functional is

$$
Q(A,I)=\max_{0\le w_p\le1}
\Bigg[\sum_{a\in A}X_w(a)-\sum_{b\in I}(X_w(b)-1)_+\Bigg].
$$

For $|A|\le M/2$ and $m=|A\setminus B|\ge1$, a proposed stability estimate states

$$
Q(A,I)\le Q(B,I)+C\,m\log(eM/m),
$$

where both sides use the same interval $I$ and length $M$, and $C$ is an absolute constant.

For $M=\Theta(n)$, this gives an $o(n)$ cost for deleting $o(n)$ source elements in the weighted formulation. It does **not** by itself justify deleting overloaded points from the target interval.

**Report:** [Residue certificates and weighted stability](reports/erdos708-residue-certificates.md)

---

## 4. Research Status

| Direction | Proposed result | Status |
|---|---|---|
| Large $M$ | $H\le2n+o(n)$ for $M\ge n^{3/2+\varepsilon}$ | Written proof; independent review pending |
| Dense $M$ | $H\le2n$ for $M\le(2+c)n$ | Written proof; independent review pending |
| Polynomially bounded shifts | $H\le2n+o(n)$ | Written proof; independent review pending |
| Arithmetic shift certificates | $H\le2n+o(n)$ for certified shifts | Written proof; independent review pending |
| Weighted stability | $O(m\log(eM/m))$ loss | Written proof; independent review pending |
| Universal bound | $g(n)\le(2+o(1))n$ | **Open** |

---

## 5. Remaining Challenges

**Intermediate interval lengths.** Existing proposed arguments leave a range between $M\approx2n$ and $M\approx n^{3/2+\varepsilon}$ without an unrestricted result.

**Arbitrary shifts.** Polynomially bounded shifts and polynomial congruence certificates do not cover the worst-case shifts.

**Overloaded interval points.** A possible strategy is to remove anomalously loaded target points and prove that only $o(n)$ source elements are left unresolved. The weighted stability theorem could then control their cost, but that transfer step is not yet proved.

**Joint divisibility.** Independent prime-factor estimates can overcount the true covering cost. Intersections of progressions and composite divisibility conditions may provide the necessary savings.

**Independent proof audit.** The newest claims require careful checking for hidden assumptions, edge cases, and possible counterexamples.

---

## 6. Repository Structure

```text
Erdos708-Research/
├── README.md
├── reports/
│   ├── REPORT.md
│   ├── erdos708-power-level-cover (1).md
│   ├── erdos708-density-and-shifts(2).md
│   ├── erdos708-residue-certificates.md
│   ├── erdos708-interval-transport (1).md
│   ├── group-deficit-and-repair.md
│   ├── bounded-prime-factors.md
│   ├── growing-prime-factors.md
│   └── four-prime-lll (1).md
├── code/
│   ├── check.py
│   ├── archive_g3.py
│   └── archive_repetitions.py
└── verification/
    ├── check_output.txt
    ├── archive_g3_output.txt
    └── archive_repetitions_output.txt
```

### Research reports

| Report | Contents |
|---|---|
| [Main research archive](reports/REPORT.md) | Earlier proofs, research directions, experiments |
| [Prime-power covering](reports/erdos708-power-level-cover%20%281%29.md) | Large-$M$ asymptotic approach |
| [Density and shifts](reports/erdos708-density-and-shifts%282%29.md) | Dense case and bounded shifts |
| [Residue certificates](reports/erdos708-residue-certificates.md) | Large shifts, weighted stability, counterexample |
| [Interval transport](reports/erdos708-interval-transport%20%281%29.md) | Transport of divisibility requirements |
| [Group deficit and repair](reports/group-deficit-and-repair.md) | Collision repair |
| [Bounded prime factors](reports/bounded-prime-factors.md) | Structural estimates |
| [Growing prime factors](reports/growing-prime-factors.md) | Extensions in factorization complexity |
| [Four-prime LLL](reports/four-prime-lll%20%281%29.md) | Four-prime structural investigations |

---

## 7. Computational Verification

Python scripts and recorded results are available under [`code/`](code/) and [`verification/`](verification/).

From the repository root:

```bash
python3 code/check.py
python3 code/archive_g3.py
python3 code/archive_repetitions.py
```

Some reports contain additional self-contained Python checks. These experiments do not establish the asymptotic claims.

The latest asymptotic results are **not claimed to be Lean-verified**.

---

## 8. Verification and Research Integrity

This project distinguishes formal proofs, written mathematical arguments, computational evidence, and conjectures. The newly reported asymptotic results are in the **written arguments pending independent verification** category.

No solution to Erdős Problem #708 is claimed. Failed approaches, counterexamples, and proof gaps are retained as part of the research record.

---

## 9. Related Research and References

- [Erdős Problems — Problem #708](https://www.erdosproblems.com/708)
- [DenisUkranian / erdos-708-research](https://github.com/DenisUkranian/erdos-708-research) — related independent research on weighted covering, block certificates, and computational constructions.

---

**Project status (November 25, 2026):** Active research. Partial results proposed; independent verification pending. The universal bound $g(n)\le(2+o(1))n$ remains open.
