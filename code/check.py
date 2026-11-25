"""Targeted constructive checks, Python 3.10+, standard library."""
from collections import Counter
from itertools import combinations
from math import gcd, prod
from random import Random


def factors(value):
    result = Counter()
    p = 2
    while p * p <= value:
        while value % p == 0:
            result[p] += 1
            value //= p
        p += 1
    if value > 1:
        result[value] += 1
    return result


def multiples(lo, size, d):
    return range(lo + (-lo) % d, lo + size, d)


def certify(values, points, lo):
    assert all(lo <= b < lo + max(values) for b in points)
    assert prod(points) % prod(values) == 0


def width_cover(values, lo):
    layers = {}
    for a in values:
        for p, e in factors(a).items():
            for j in range(1, e + 1):
                layers.setdefault((p, j), set()).add(a)
    supports = sorted(set(map(frozenset, layers.values())), key=lambda s: (len(s), sorted(s)))
    points = set()
    charged = {a: [] for a in values}
    for support in supports:
        d = gcd(*support)
        need = len(support) - sum(b % d == 0 for b in points)
        if need <= 0:
            continue
        available = [a for a in sorted(support) if all(not t < support for t in charged[a])]
        assert len(available) >= need
        for a in available[:need]:
            charged[a].append(support)
        for b in multiples(lo, max(values), d):
            if b not in points:
                points.add(b)
                need -= 1
                if not need:
                    break
        assert need == 0
    for sets in charged.values():
        assert all(not (s <= t or t <= s) for s, t in combinations(sets, 2))
    assert sum(map(len, charged.values())) == len(points)
    certify(values, points, lo)


def match(tasks, lo, size, forbidden):
    owner = {}
    def place(i, visited):
        d, p, _ = tasks[i]
        for b in multiples(lo, size, d*p):
            if b in forbidden or b in visited:
                continue
            visited.add(b)
            if b not in owner or place(owner[b], visited):
                owner[b] = i
                return True
        return False
    for i in range(len(tasks)):
        if not place(i, set()):
            return None
    return owner


def core_cover(rows, lo, joint):
    values = [prod(row) for row in rows]
    assert len(set(values)) == len(values)
    size = max(values)
    reserve = next(iter(multiples(lo, size, values[0])))
    groups = {}
    for row in rows[1:]:
        groups.setdefault(0 if joint else row[0], []).append(row)
    buckets = {}
    for group in groups.values():
        assignment = match(group, lo, size, {reserve})
        if assignment is None:
            return None
        for b, i in assignment.items():
            buckets.setdefault(b, []).append(group[i])
    points = {reserve, *buckets}
    remaining = []
    bad = 0
    for b, group in buckets.items():
        cores = prod(d for d, _, _ in group)
        assert b % cores == 0
        free = next((i for i, (_, p, _) in enumerate(group) if b % (cores*p) == 0), None)
        bad += free is None
        for i, (_, p, r) in enumerate(group):
            remaining.append(r)
            if i != free:
                remaining.append(p)
    target = prod(values) // prod(remaining)
    total = prod(points)
    assert total % target == 0
    for p in remaining:
        target *= p
        if total % target:
            b = next(b for b in multiples(lo, size, p) if b not in points)
            points.add(b)
            total *= b
    assert len(points) <= 2 * len(values) - 1 + bad
    certify(values, points, lo)
    return bad


def main():
    rng = Random(7082511)
    for _ in range(160):
        width_cover(rng.sample(range(2, 100), rng.randrange(2, 13)), rng.randrange(1, 5000))
    print("160 layer-support covers: divisibility and charge antichains verified")
    # Multiple internal primes per core. Outer primes may occur inside a core.
    pool = {d*p*r: (d,p,r) for d in (35, 143, 17) for p in (2,3,5)
            for r in (5,7,11,13,17,19) if p <= r}
    for _ in range(75):
        rows = rng.sample(list(pool.values()), 16)
        assert core_cover(rows, rng.randrange(1, 100000), False) == 0
    print("75 coprime-core covers with repeated primes: divisibility and 2n-1 verified")
    pool = {d*p*r: (d,p,r) for d in (30,42,70) for p in (2,3,5)
            for r in (7,11,13,17,19)}
    for _ in range(75):
        rows = rng.sample(list(pool.values()), 20)
        assert core_cover(rows, rng.randrange(1, 100000), True) == 0
    print("75 overlapping-core samples: global match found and 2n-1 verified")
    # A bad local certificate, even though each individual assignment is legal.
    b = 210
    rows = [(6,5,11),(35,2,3)]
    assert len({prod(row) for row in rows}) == 2
    assert all(b % (d*p) == 0 for d,p,r in rows)
    assert all(b % (210*p) != 0 for d,p,r in rows)
    print("2-cycle at 210 verified (local obstruction only)")


if __name__ == "__main__":
    main()
