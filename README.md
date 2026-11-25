# Erdős–Surányi Problem #708

### Independent Research in Number Theory and Combinatorics

Research repository dedicated to **Erdős Problem #708**, with a focus on asymptotic bounds, prime-power coverings, combinatorial methods, and computational verification.

> **Status — November 2026**
>
> Several new partial asymptotic results have been proposed.
> The universal asymptotic bound remains open.
> The latest proofs are awaiting independent mathematical verification.

---

## 1. Main Problem

Let

$$
A=\{a_1,\ldots,a_n\}\subseteq\{2,\ldots,M\},
\qquad M=\max A,
$$

where all elements of \(A\) are distinct.

Let \(I\) be an interval of \(M\) consecutive positive integers.

Define

$$
\tau(A,I)=
\min\left\{
|B|:
B\subseteq I,\quad
\prod_{a\in A}a\mid\prod_{b\in B}b
\right\}.
$$

Then

$$
g(n)=\sup_{A,I}\tau(A,I).
$$

### Main Research Objective

Establish the universal asymptotic upper bound

$$
\boxed{g(n)\le (2+o(1))n.}
$$

This remains the **central open objective** of the project.

---

## 2. Prime-Power Covering Framework

A central tool is the stronger covering quantity

$$
H(A,I)=
\min_{\substack{B\subseteq I\\
C_B(p^j)\ge C_A(p^j)\ \forall p^j\le M}}
|B|,
$$

where

$$
C_X(q)=|\{a\in X:q\mid a\}|.
$$

Because covering every prime-power level implies the required product divisibility,

$$
\boxed{\tau(A,I)\le H(A,I).}
$$

Much of the research aims to prove

$$
H(A,I)\le 2n+o(n)
$$

in increasingly general parameter ranges.

---

## 3. Main Research Results

The following results are presented in the linked research reports.

**Important:** These are proposed mathematical theorems supported by written arguments. They have not yet undergone independent formal verification or complete external peer review.

### 3.1. Large-\(M\) Asymptotic Bound

For every fixed \(\varepsilon>0\), the project proposes

$$
\boxed{
M\ge n^{3/2+\varepsilon}
\quad\Longrightarrow\quad
H(A,I)\le 2n+O_\varepsilon(n^{1-c_\varepsilon})
}
$$

for some \(c_\varepsilon>0\), uniformly over all admissible families and interval shifts.

Main techniques:

- Unitary decomposition of prime-power atoms.
- Greedy extraction of common divisors.
- Probabilistic injection and matching.
- Collision estimates using gcd sums.
- Repair of uncovered prime-power levels.

**Report:**

[Prime-Power-Level Covering](reports/erdos708-power-level-cover%20%281%29.md)

### 3.2. Dense-Interval Bound

A second proposed theorem establishes that there exists an absolute constant \(c>0\) such that, for sufficiently large \(n\),

$$
\boxed{
M\le(2+c)n
\quad\Longrightarrow\quad
H(A,I)\le2n
}
$$

uniformly over all interval shifts.

The argument uses:

- Near-saturated prime-power progressions.
- Second-, third-, and fourth-moment estimates.
- Density restrictions.
- Fractional covering and rounding.

The argument does not provide an explicit numerical value of \(c\).

**Report:**

[Density and Shifts](reports/erdos708-density-and-shifts%282%29.md)

### 3.3. Polynomially Bounded Shifts

For fixed \(\varepsilon>0\) and \(K\ge1\), another proposed result covers

$$
M\ge n^{1+\varepsilon},
\qquad x+M\le M^K,
$$

where \(I=(x,x+M]\).

Under these assumptions,

$$
H(A,I)\le2n+O_{\varepsilon,K}(n^{1-\eta})
$$

for some \(\eta>0\).

This extends the near-\(2n\) covering method into the intermediate range, but does not handle arbitrary shifts.

**Report:**

[Density and Shifts](reports/erdos708-density-and-shifts%282%29.md)

### 3.4. Arithmetic Certificates for Large Shifts

The latest investigation introduces polynomial certificates.

Let

$$
L_M=\operatorname{lcm}(1,2,\ldots,M).
$$

Suppose an interval shift \(x\) satisfies

$$
F(x)\equiv0\pmod{L_M},
$$

where \(F\in\mathbb Z[X]\) is a nonzero polynomial of bounded degree with polynomially bounded coefficients.

Under the conditions specified in the report, the proposed result is

$$
\boxed{
H(A,I)\le2n+O(n^{1-\eta}).
}
$$

This can apply to certain astronomically large shifts.

However, these certificates do not cover all residue classes, so the universal problem remains open.

**Report:**

[Residue Certificates and Weighted Stability](reports/erdos708-residue-certificates.md)

### 3.5. Weighted Covering and Stability

The research also investigates an LP-dual functional

$$
Q(A,I)=
\max_{0\le w_p\le1}
\left[
\sum_{a\in A}X_w(a)
-
\sum_{b\in I}(X_w(b)-1)_+
\right],
$$

where

$$
X_w(a)=\sum_p w_pv_p(a).
$$

A proposed stability theorem states that, for \(|A|\le M/2\),

$$
\boxed{
Q(A,I)\le
Q(B,I)+C\,m\log\left(\frac{eM}{m}\right),
}
$$

where \(m=|A\setminus B|\ge1\), with the comparison carried out at the same interval length \(M\).

In the dense regime \(M=\Theta(n)\), removing \(o(n)\) exceptional source elements therefore costs only \(o(n)\) in the weighted formulation.

This may help control exceptional configurations in future proofs.

**Report:**

[Residue Certificates and Weighted Stability](reports/erdos708-residue-certificates.md)

---

## 4. Current Research Status

| Research direction | Proposed bound or result | Verification status |
|---|---|---|
| Large \(M\) | \(2n+o(n)\) for \(M\ge n^{3/2+\varepsilon}\) | Written proof; independent review pending |
| Dense \(M\) | \(2n\) for \(M\le(2+c)n\) | Written proof; independent review pending |
| Polynomially bounded shifts | \(2n+o(n)\) | Written proof; independent review pending |
| Arithmetic shift certificates | \(2n+o(n)\) for certified shifts | Written proof; independent review pending |
| Weighted stability | \(O(m\log(eM/m))\) loss | Written proof; independent review pending |
| Universal asymptotic | \(g(n)\le(2+o(1))n\) | **OPEN** |

These statements describe the current project claims, not independently established results.

---

## 5. Remaining Challenges

The principal unsolved issue is to establish a uniform bound for **all** admissible families and **all** interval shifts.

### Intermediate Interval Lengths

The proposed large-\(M\) and dense-\(M\) theorems do not cover the entire range between

$$
M\approx2n
\qquad\text{and}\qquad
M\approx n^{3/2+\varepsilon}.
$$

Partial intermediate-range results have additional restrictions on shifts.

### Arbitrarily Large Shifts

Certain shifts create exceptional concentrations of divisibility requirements.

Polynomially bounded shifts and polynomial congruence certificates do not cover the worst-case situation.

### Overloaded Interval Points

A promising direction is to prove that highly overloaded target points can be discarded while leaving only \(o(n)\) source elements unresolved.

The weighted stability theorem could then control the cost of those exceptional source elements.

The missing step is a uniform theorem connecting removal of overloaded target points to a small exceptional set of source elements.

### Joint Divisibility

Simple independent prime-factor estimates can overcount the true covering cost.

Composite divisibility constraints, intersections of progressions, and weighted compensation may provide sharper estimates.

---

## 6. Repository Structure

```text
Erdos708-Research/
│
├── README.md
│
├── reports/
│   ├── REPORT.md
│   ├── erdos708-power-level-cover (1).md
│   ├── erdos708-density-and-shifts(2).md
│   ├── erdos708-residue-certificates.md
│   ├── erdos708-interval-transport (1).md
│   ├── group-deficit-and-repair.md
│   └── ...
│
├── code/
│   ├── check.py
│   ├── archive_g3.py
│   └── archive_repetitions.py
│
└── verification/
    ├── check_output.txt
    ├── archive_g3_output.txt
    └── archive_repetitions_output.txt
```

### Research Reports

| Document | Contents |
|---|---|
| [Main Archive](reports/REPORT.md) | Earlier proofs, research directions, and experiments |
| [Prime-Power Covering](reports/erdos708-power-level-cover%20%281%29.md) | Large-\(M\) asymptotic method |
| [Density and Shifts](reports/erdos708-density-and-shifts%282%29.md) | Dense intervals and polynomially bounded shifts |
| [Residue Certificates](reports/erdos708-residue-certificates.md) | Large shift certificates, weighted stability, counterexample |
| [Interval Transport](reports/erdos708-interval-transport%20%281%29.md) | Transport of divisibility requirements |
| [Group Deficit and Repair](reports/group-deficit-and-repair.md) | Collision repair and group deficits |
| [Bounded Prime Factors](reports/bounded-prime-factors.md) | Structural estimates |
| [Growing Prime Factors](reports/growing-prime-factors.md) | Extensions involving prime-factor complexity |

---

## 7. Computational Verification

The repository includes Python experiments and recorded verification outputs.

To reproduce the existing computations:

```bash
python3 code/check.py
python3 code/archive_g3.py
python3 code/archive_repetitions.py
```

Additional self-contained computational tests are included in individual reports.

**Computational verification is not a substitute for a complete mathematical proof.**

The newest asymptotic statements have not been independently Lean-verified.

---

## 8. Verification and Research Integrity

This repository distinguishes:

1. **Formal proofs:** statements independently checked in a proof assistant.
2. **Mathematical arguments:** written proofs awaiting external verification.
3. **Computational evidence:** finite experiments with reproducible code.
4. **Conjectures:** statements not yet established.

No claim of solving Erdős Problem #708 is made.

Possible gaps, incorrect lemmas, and failed approaches are considered part of the research record.

Independent mathematical review and counterexample searches are encouraged.

---

## 9. Related Research

Related independent investigations:

[DenisUkranian / erdos-708-research](https://github.com/DenisUkranian/erdos-708-research)

Topics of potential connection include:

- Weighted covering formulations.
- Two-block certificates.
- Deficit and repair methods.
- Prime-power multiplicities.
- Computational counterexamples.
- Exceptional divisibility patterns.

---

## 10. References

- [Erdős Problems — Problem #708](https://www.erdosproblems.com/708)
- [Related Erdős–Surányi Research](https://github.com/DenisUkranian/erdos-708-research)

---

### Project Status

**November 25, 2026**

- Partial asymptotic results proposed.
- Several new mathematical methods developed.
- Written proof reports available.
- Independent verification pending.
- Universal coefficient \(2\) remains unproved.

**Main goal:**

$$
\boxed{g(n)\le(2+o(1))n.}
$$
