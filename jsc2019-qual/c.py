n = int(input())
s = int(input())

dp = [[0 for x in s] for y in range(n)]
dp[0][0] = 0

for i in range(n):
    for j in range(2*n):
        if j <= i:
            continue
        if s[j] == 'W':
