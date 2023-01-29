from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

N, M = [int(x) for x in input().split(" ")]
Ss = [0] * N
bulbs = []
for i in range(M):
    s = [int(x) for x in input().split(" ")]
    k = s[0]
    ss = set(s[1:])
    bulbs.append(ss)
ps = [int(x) for x in input().split(" ")]
bulbs = list(zip(bulbs, ps))

def checkPattern(subset, bs, p):
    inter = subset.intersection(bs)
    res = len(inter) % 2 == p
    return res

count = 0
for subset in powerset(set(range(1, N+1))):
    subset = set(subset)
    pts = [checkPattern(subset, bs, p) for bs, p in bulbs]
    if all(pts):
        count += 1

print(count)
