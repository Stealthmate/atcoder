BLACK = '#'
WHITE = '.'
START = 'S'
GOAL = 'G'

h, w, t = map(int, input().split(" "))
Gm = [input() for i in range(h)]

start = None
goal = None

for i in range(h):
    for j in range(w):
        if Gm[i][j] == START:
            start = (i, j)
        if Gm[i][j] == GOAL:
            goal = (i, j)

def dijkstra(V, adjL, x):
    dist = { x: int(10e20) for x in V }
    pred = { x: None for x in V }

    dist[x] = 0

    Q = set(V)
    while Q:
        n = min(Q, key=lambda x: dist[x])
        Q.remove(n)

        for p, w in adjL[n]:
            alt = dist[n] + w
            if alt < dist[p]:
                dist[p] = alt
                pred[p] = n

    return dist, pred

V = [(x, y) for x in range(h) for y in range(w)]
class Adj:
    def __init__(self, x):
        self.x = x
    def __getitem__(self, key):
        i, j = key
        def res(x, y):
            return (x, y), self.x if Gm[x][y] == BLACK else 1

        if i > 0:
            yield res(i-1, j)
        if i < h - 1:
            yield res(i+1, j)
        if j > 0:
            yield res(i, j-1)
        if j < w - 1:
            yield res(i, j+1)

low = 0
high = t
x = 0
while low < high - 1:
    x = (low + high) // 2
    dist, pred = dijkstra(V, Adj(x), start)
    # print(low, high, x, dist[goal])
    p = pred[goal]
    # while p:
    #     print(p)
    #     p = pred[p]
    if dist[goal] > t:
        high = (low + high) // 2
    else:
        low = (low + high) // 2
x = (low + high) // 2
print(x)
