N, m = map(int, input().split(" "))
edges = [tuple(map(int, input().split(" "))) for i in range(m)]

nodes = {}
for a, b in edges:
    if a not in nodes:
        nodes[a] = set()
    if b not in nodes:
        nodes[b] = set()
    nodes[a].add(b)
    nodes[b].add(a)

ans = {k: set() for k in nodes.keys()}
for n, frs in nodes.items():
    for f in frs:
        ans[n] = ans[n] | (nodes[f] - frs - set([n]))

for k in range(1, N + 1):
    print(len(ans[k]) if k in ans else 0)
