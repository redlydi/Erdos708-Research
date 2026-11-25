"""Запись выполненной в предыдущем этапе короткой проверки; Python 3."""
from itertools import combinations
from math import gcd, prod
from random import Random
rng = Random(708)

def factors(a):
    f = {}
    p = 2
    while p*p <= a:
        while a % p == 0:
            f[p] = f.get(p, 0) + 1
            a //= p
        p += 1
    if a > 1:
        f[a] = 1
    return f

def exact(A, L):
    P = prod(A)
    states = {P: 0}
    for b in range(L, L + max(A)):
        for r, k in list(states.items()):
            v = r // gcd(r, b)
            states[v] = min(states.get(v, k+1), k+1)
    return states[1]

for _ in range(250):
    A = rng.sample(range(2, 32), rng.randint(1, 6))
    fs = [factors(a) for a in A]
    exc = sum(max(sum(p in f for f in fs)-2, 0) for p in set().union(*fs))
    assert exact(A, rng.randrange(1, 600)) <= len(A)*4//3 + exc

print('250 small comparisons;', exact([77,91,143],5935), 'for triangle;',
      [b for b in range(5935,6078) if b % 169 == 0])
