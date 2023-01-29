n, m = map(int, input().split(" "))
xyzs = [tuple(map(int, input().split(" "))) for i in range(n)]
D = list(0 for i in range(m))

s = 0
for x, y, z in xyzs:
    D[x-1] += z
    if y < m:
        D[y] -= z
    s += z

for i in range(1, m):
    D[i] += D[i-1]

print(s - min(D))
