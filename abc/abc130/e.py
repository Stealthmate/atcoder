n, m = map(int, input().split(" "))
s = list(map(int, input().split(" ")))
t = list(map(int, input().split(" ")))

dp = [[0] * m for i in s]
ans = [[0] * m for i in s]

for i in range(n):
    for j in range(m):
        ans[i][j] = (ans[i-1][j] if i > 0 else 0) + (ans[i][j-1] if j > 0 else 0) - (ans[i-1][j-1] if i > 0 and j > 0 else 0)
        if s[i] == t[j]:
            ans[i][j] += (ans[i-1][j-1] if i > 0 and j > 0 else 0) + 1

print((ans[-1][-1] + 1) % (1000000007))
