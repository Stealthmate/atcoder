from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(2, len(s)+1))

n = int(input())
xys = zip(*[tuple(map(int, input().split(" "))) for i in range(n)])

xys_h = sorted(xys[0])
xys_v = sorted(xys[1])

xys = zip(xys[0], xys[1], xys_h, xys_v)

M = [[0 for x in range(n + 1)] for x in range(n + 1)]

ans = 0
for s in powerset(xys):
    amin = min(s, key=lambda x: x[0])
    amax = max(s, key=lambda x: x[0])

    bmin = max(s, key=lambda x: x[1])
    bmax = max(s, key=lambda x: x[1])

    M[amin[2]][amin[3]] += 1
    M[amax[2] + 1][amin[3]] -= 1
    M[amin[2]][
