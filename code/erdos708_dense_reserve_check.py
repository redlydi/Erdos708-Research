"""Exact constants for the dense reserve and examples of the profile coupling.
Python 3. No external packages. Run: python3 erdos708_dense_reserve_check.py
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import ceil, comb, prod


def upper_bad_density(mesh=512, scale=10**12):
    end = ceil(F(200, 33) * mesh)
    low = [[scale] * (end + 1)] + [[0] * (end + 1) for _ in range(5)]
    high = [[scale] * (end + 1)] + [[0] * (end + 1) for _ in range(5)]
    for k in range(1, 6):
        for i in range(k * mesh, end):
            low[k][i + 1] = low[k][i] + low[k - 1][i - mesh] // (i + 1)
            high[k][i + 1] = high[k][i] + (high[k - 1][i + 1 - mesh] + i - 1) // i
    return F(high[3][end] - 3 * low[4][end - 1] + 6 * high[5][end]
             + high[2][3 * mesh], scale)


def check_local_reserve():
    count = 0
    for s, w1, w2, eligible in product(range(31), range(21), range(21), (False, True)):
        x = s + w1 + w2
        if s >= 20:
            base, credit = 20, 0
        else:
            h = 20 - s
            v1, v2 = min(w1, h), min(w2, h)
            base = s + v1 + v2
            credit = max(0, v1 + v2 - h) if eligible else 0
        g12 = 12 * (min(40, x) - base) + 11 * credit
        assert F(g12, 24) >= F(5, 18) * credit
        shortfall12 = 12 * (40 - base) + 11 * credit
        if F(shortfall12, 12) < F(20, 8):
            assert s < F(20, 8) and min(w1, w2) > F(7 * 20, 8)
        count += 1
    return count


def val(number, p):
    exponent = 0
    while number % p == 0:
        exponent += 1
        number //= p
    return exponent


def profile_coupling(M, shift, core=(2, 3), tail=(7, 11, 13, 17, 19)):
    assert sum(F(1, p) for p in tail) <= F(1, 2)
    source = range(1, M + 1)
    target = range(shift + 1, shift + M + 1)

    def core_at(t):
        return tuple(val(t, p) for p in core)

    rows = defaultdict(list)
    squareful = 0
    for a in source:
        active = [p for p in tail if a % p == 0]
        if any(a % (p * p) == 0 for p in active):
            squareful += 1
        elif len(active) >= 2:
            rows[prod(active[:-1]), core_at(a)].append(a)

    slots = defaultdict(list)
    seen = set()
    for d in sorted({d for d, _ in rows}):
        first = (shift // d + 1) * d
        for b in range(first, shift + M + 1, d):
            if all((b // d) % p for p in tail if d * p <= M):
                assert b not in seen
                seen.add(b)
                slots[d, core_at(b)].append(b)
    matching = {}
    missed_banks = 0
    for key, group in rows.items():
        matching.update(zip(group, slots[key]))
        missed_banks += max(0, len(group) - len(slots[key]))

    remaining_rows, remaining_slots = defaultdict(list), defaultdict(list)
    used = set(matching.values())
    for a in source:
        if a not in matching:
            remaining_rows[core_at(a)].append(a)
    for b in target:
        if b not in used:
            remaining_slots[core_at(b)].append(b)
    for key, group in remaining_rows.items():
        matching.update(zip(group, remaining_slots[key]))
    used = set(matching.values())
    leftovers = [a for a in source if a not in matching]
    matching.update(zip(leftovers, [b for b in target if b not in used]))
    assert len(set(matching.values())) == len(matching) == M
    discrepancy = sum((Counter(map(core_at, source)) - Counter(map(core_at, target))).values())
    assert len(leftovers) == discrepancy
    bad = sum(any(val(a, p) > val(b, p) for p in core)
              or sum(max(0, val(a, p) - val(b, p)) for p in tail) > 1
              for a, b in matching.items())
    assert bad <= squareful + missed_banks + discrepancy
    return (M, shift, squareful, missed_banks, discrepancy, bad)


if __name__ == "__main__":
    for k in range(7):
        assert int(k >= 3) <= comb(k, 3) - 3 * comb(k, 4) + 6 * comb(k, 5)
    bad_prob = upper_bad_density()
    assert bad_prob < F(303, 1000)
    d = F(1, 3) - F(303, 1000)
    gain = F(9, 32000) * d**2
    assert gain > F(1, 4_000_000)
    beta, eta = F(1, 10**60), F(1, 10**22)
    assert 618 * beta < eta / 4
    assert F(1, 10**50) + 12 * beta / eta < F(1, 10**32)
    assert 10**5 * (140 * eta + F(16, 10**32)) < F(1, 10**12)
    assert gain - F(2, 10**12) > F(2, 10**7)
    mixed_overloads = [(i, j) for i in range(7) for j in range(4)
                       if 144*i + 269*j <= 1000 and 30*i + 55*j > 200]
    assert mixed_overloads == [(5, 1)]
    print("Upper bad-row density:", bad_prob, float(bad_prob))
    print("Lower asymptotic saving at n/M=1/3:", gain, float(gain))
    print("Local identities checked:", check_local_reserve())
    print("M, shift, squareful rows, unmatched requests, core discrepancy, bad pairs")
    for m in (210, 1001, 4096):
        for t in (0, 317, 10**30 + 117):
            print(*profile_coupling(m, t))
