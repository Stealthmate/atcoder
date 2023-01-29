from collections import deque

r, c = map(int, input().split(" "))
sy, sx = map(int, input().split(" "))
gy, gx = map(int, input().split(" "))
g = [list(input()) for i in range(r)]


Q = deque()
Q.appendleft((sx - 1, sy - 1, 1))
seen = set()
while Q:
    x, y, p = Q.pop()
    if (x, y) in seen:
        continue
    seen.add((x, y))

    ns = [ (a, b, p + 1) for a, b in [(x, min(y + 1, r - 1)), (x, max(y - 1, 0)), (max(x - 1, 0), y), (min(x + 1, c - 1), y)] if (a, b) ]

    if (gx - 1, gy - 1) in [(a,b) for a, b, _ in ns]:
        print(p)
        exit(0)
    ns = filter(lambda i: g[i[1]][i[0]] == '.', ns)
    Q.extendleft(ns)
