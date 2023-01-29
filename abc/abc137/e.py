def bf(v, ew, s):
    d = [99999999999999999999999999 for x in v]
    p = [None for x in v]
    d[s] = 0
    p[s] = None

    for i in range(1, len(v) - 1):
       for x, y, w in ew:
           if d[x] + w < d[y]:
               d[y] = d[x] + w
               p[y] = x

    for x, y, w in ew:
        if d[x] + w < d[y] and canReach(y):
            return None

    return d

n, m, p = map(int, input().split(" "))
edges = []
for i in range(m):
    a, b, c = map(int, input().split(" "))
    edges.append((a - 1, b - 1, -(c - p)))

ans = bf(range(n), edges, 0)
if not ans:
    print(-1)
else:
    print(-ans[n - 1])
