import numpy as np

n = int(input())
a = np.array([list(map(int, input().split(" "))) for i in range(n)])
ans = 0

edges = np.ones((n, n))

class BadBoard(Exception):
    pass

try:
    for i in range(n):
        for j in range(n):
            path = a[i][j]
            for k in range(n):
                if a[i][k] + a[k][j] < a[i][j]:
                    raise BadBoard
                elif a[i][k] + a[k][j] == a[i][j] and i != k and j != k:
                    edges[i][j] = 0

    print(int(np.sum(edges * a) // 2))

except BadBoard:
    print(-1)
