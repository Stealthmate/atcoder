from collections import Counter

n, m = map(int, input().split(" "))
r = zip(*[list(map(int, input().split(" "))) for i in range(m)])
r = list(r)
c1 = dict(Counter(r[0]).most_common())
c2 = dict(Counter(r[1]).most_common())
for i in range(1, n + 1):
    print((c1[i] if i in c1 else 0) + (c2[i] if i in c2 else 0))
