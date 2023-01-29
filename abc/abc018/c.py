r, c, k = map(int, input().split(" "))

WHITE = 'o'
BLACK = 'x'

s = [input() for i in range(r)]

up = [[0] * c for i in range(r)]
down = [[0] * c for i in range(r)]

for j in range(c):
    lastUp = 0
    lastDown = 0
    for i in range(r):
        if s[i][j] == BLACK:
            lastUp = 0
        else:
            lastUp += 1

        if s[r - 1 - i][j] == BLACK:
            lastDown = 0
        else:
            lastDown += 1

        up[i][j] = lastUp
        down[r - 1 - i][j] = lastDown


ans = 0
for i in range(k - 1, r - k + 1):
    for j in range(k - 1, c - k + 1):
        ok = True
        for l in range(j - k + 1, j + k):
            if up[i][l] < k - abs(j - l) or down[i][l] < k - abs(j - l):
                ok = False
                break
        if ok:
            ans += 1

print(ans)
