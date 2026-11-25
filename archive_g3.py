"""Exact finite part and independent constructive stress tests. Python 3.10+."""
from bisect import bisect_right
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, prod
from random import Random


def primes_up_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes(1 + (n - p*p) // p)
    return [p for p in range(n + 1) if sieve[p]]


def finite_certificate():
    primes = primes_up_to(1_000_000)
    count = 0
    for length in range(4, 513):
        active = primes[:bisect_right(primes, isqrt(length))]
        quota = {p: bisect_right(primes, length // p) - i
                 for i, p in enumerate(active)}
        for size in range(1, len(active) + 1):
            for subset in combinations(active, size):
                d = sum(length // p for p in subset)
                t = sum(quota[p] for p in subset)
                e = sum((length + p*q - 1) // (p*q)
                        for p, q in combinations(subset, 2))
                if d*d <= t*(d + 2*e):
                    raise AssertionError((length, subset))
                count += 1
    lower, blocks, worst = 513, 0, Fraction(0)
    while lower < 1_000_000:
        upper = min(999_999, lower + lower // 100)
        active = primes[:bisect_right(primes, isqrt(upper))]
        quota = [bisect_right(primes, upper // p) - i
                 for i, p in enumerate(active)]
        alpha = max(Fraction(t, lower // p) for p, t in zip(active, quota))
        c = 1 - Fraction(1, isqrt(lower))
        score = alpha + Fraction(2 * sum(quota), lower) / c**2
        if score >= 1:
            raise AssertionError((lower, upper, score))
        worst = max(worst, score)
        blocks += 1
        lower = upper + 1
    print(f"finite certificate: {count} subsets, {blocks} blocks, max score {worst}")


def layer_certificate():
    primes = primes_up_to(1_000_000)
    count = 0
    for length in range(4, 601):
        active = primes[:bisect_right(primes, isqrt(length))]
        quota = {p: bisect_right(primes, length // p) - i
                 for i, p in enumerate(active)}
        for size in range(1, len(active) + 1):
            for subset in combinations(active, size):
                q = primes[bisect_right(primes, subset[-1])]
                d = sum(m - (m + q - 1) // q for m in
                        (length // p for p in subset))
                t = sum(quota[p] for p in subset)
                e = sum((length + p*r - 1) // (p*r)
                        for p, r in combinations(subset, 2))
                if d*d <= (t - 1)*(d + 2*e):
                    raise AssertionError((length, subset, q))
                count += 1
    lower, checks, worst = 601, 0, Fraction(0)
    while lower < 1_000_000:
        upper = min(999_999, lower + lower // 100)
        for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            limit = isqrt(upper) if q == 31 else min(isqrt(upper), q - 1)
            active = primes[:bisect_right(primes, limit)]
            quota = [bisect_right(primes, upper // p) - i
                     for i, p in enumerate(active)]
            capacity = [m - (m + q - 1) // q for m in
                        (lower // p for p in active)]
            alpha = max(Fraction(t, d) for t, d in zip(quota, capacity))
            c = min(Fraction(d*p, upper) for d, p in zip(capacity, active))
            beta = Fraction(sum(quota), lower)
            score = alpha + beta * (1 + Fraction(active[-1]**2, lower)) / c**2
            if score >= 1:
                raise AssertionError((lower, upper, q, score))
            worst = max(worst, score)
            checks += 1
        lower = upper + 1
    print(f"layer certificate: {count} subsets, {checks} block checks, max score {worst}")


def factor_list(a):
    result = []
    p = 2
    while p*p <= a:
        while a % p == 0:
            result.append(p)
            a //= p
        p += 1
    if a > 1:
        result.append(a)
    return result


def build_cover(records, start, layered=False):
    # A record is (a, None) for rank <= 2, or (a, (p,q,e,r)).
    # The callers supply a single exponent e for each pivot q.
    length = max(a for a, _ in records)
    end = start + length
    first = lambda d: start + (-start) % d
    reserved = None if layered else first(records[0][0])
    chosen = set() if layered else {reserved}
    groups = defaultdict(list)
    for a, representation in (records if layered else records[1:]):
        if representation:
            p, q, e, r = representation
            assert a == p*q**e*r and p <= min(q, r)
            assert not layered or p < q
            groups[q, e].append((p, e))
    for (q, exponent), tasks in groups.items():
        if not layered:
            assert sum(other_q == q for other_q, _ in groups) == 1
        owner = {}
        def augment(task, visited):
            p, e = tasks[task]
            step = p*q**e
            for b in range(first(step), end, step):
                if layered and b % (q**(exponent + 1)) == 0:
                    continue
                if b == reserved or b in visited:
                    continue
                visited.add(b)
                if b not in owner or augment(owner[b], visited):
                    owner[b] = task
                    return True
            return False
        for task in range(len(tasks)):
            if not augment(task, set()):
                raise AssertionError(("matching", q, tasks, start))
        chosen.update(owner)
    target = prod(a for a, _ in records)
    residual = target // gcd(target, prod(chosen))
    # Factor only the input moduli, never the potentially huge residual.
    for p in sorted({p for a, _ in records for p in factor_list(a)}):
        for b in range(first(p), end, p):
            if residual % p:
                break
            if b not in chosen:
                chosen.add(b)
                residual //= gcd(residual, b)
    assert residual == 1 and prod(chosen) % target == 0
    assert all(start <= b < end for b in chosen)
    assert len(chosen) <= 2*len(records) - int(not layered)
    return chosen


def experiments():
    rng = Random(708031)
    candidates = []
    for a in range(2, 420):
        factors = factor_list(a)
        if len(factors) <= 3:
            rep = None
            if len(factors) == 3:
                p, q, r = factors
                rep = (p, q, 1, r)
            candidates.append((a, rep))
    for _ in range(500):
        build_cover(rng.sample(candidates, rng.randrange(1, 70)),
                    rng.randrange(1, 10**13))
    primes = primes_up_to(13)
    pool = {}
    for q in primes:
        e = 1 + (q % 3)
        for p in primes:
            for r in primes:
                if p <= min(q, r):
                    a = p*q**e*r
                    pool[a] = (a, (p, q, e, r))
    for _ in range(200):
        records = rng.sample(list(pool.values()), rng.randrange(3, 35))
        build_cover(records, rng.randrange(1, 10**12))
    layered_pool = {}
    for q in [3, 5, 7]:
        for e in [1, 2, 3]:
            for p in primes:
                for r in primes:
                    if p < q and p <= r:
                        a = p*q**e*r
                        layered_pool[a] = (a, (p, q, e, r))
    for _ in range(250):
        records = rng.sample(list(layered_pool.values()), rng.randrange(5, 50))
        build_cover(records, rng.randrange(1, 10**10), layered=True)
    print("constructive checks: 250 variable-exponent families")
    print("constructive checks: 500 rank-three, 200 prime-power pivot families")


if __name__ == "__main__":
    finite_certificate()
    layer_certificate()
    experiments()
