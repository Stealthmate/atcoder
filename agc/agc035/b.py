from collections import deque

N, M = map(int, input().split(" "))
edges = set([tuple(map(int, input().split(" "))) for i in range(M)])
edgesDict = {i: set() for i in range(1, N + 1)}
for e in edges:
    edgesDict[e[0]].add(e[1])
    edgesDict[e[1]].add(e[0])

newEs = []
for i in range(1, N + 1):
    es = [e for e in edgesDict[i] if len(edgesDict[e]) % 2 == 1]
    if len(es) % 2 == 1:
        edgesDict[i].remove(es[0])
        edgesDict[es[0]].remove(i)
        newEs.append((es[0], i))
        es = es[1:]
    for e in es:
        edgesDict[i].remove(e)
        edgesDict[e].remove(i)
    newEs.extend([(i, e) for e in es])

if any(len(x) > 0 for x in edgesDict.values()):
    print(-1)
    exit(0)

for e in newEs:
    print(e[0], e[1])
