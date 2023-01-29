from math import floor, ceil
n = int(input())
a = [tuple(map(int, input().split(" "))) for i in range(n)]
K = 1000000
D = list(0 for i in range(K + 1))

for x, y in a:
    D[x] += 1
    if y < K:
        D[y+1] -= 1

M = 0
for i in range(0, K + 1):
    if i > 0:
        D[i] += D[i-1]
    M = max(M, D[i])

print(M)
