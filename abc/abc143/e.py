N, M, L = map(int, input().split(" "))

edges = [tuple(map(int, input().split(" "))) for i in range (M)]
edges = [(x-1, y-1, w) for (x, y, w) in edges if w <= L]

def wf(V, E):
    dist = [[int(1e25)] * len(V) for i in range(len(V))]
    for x, y, w in E:
        dist[x][y] = w
        dist[y][x] = w

    for v in V:
        dist[v][v] = 0

    for k in range(0, len(V)):
        for i in range(0, len(V)):
            for j in range(0, len(V)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k]+ dist[k][j]

    return dist

dist = wf(range(N), edges)

dist_E = []
for i in range(N):
    for j in range(N):
        if dist[i][j] <= L:
            dist_E.append((i, j, 1))
            dist_E.append((j, i, 1))

dist1 = wf(range(N), dist_E)

Q = int(input())
for i in range(Q):
    s, t = map(int, input().split(" "))
    s -= 1
    t -= 1

    if dist1[s][t] > 1000:
        print(-1)
    else:
        print(dist1[s][t] - 1)
