l = input()

dp = [[0, 0]] * len(l)

dp[0][0] = 1
dp[0][1] = 2

MOD = 1000000007

for i in range(1, len(l)):
    if l[i] == '0':
        dp[i][0] = (dp[i-1][0] * 3) % MOD
        dp[i][1] = dp[i-1][1] % MOD
    else:
        dp[i][0] = (3*dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = (dp[i-1][1] * 2) % MOD

print((dp[-1][0] + dp[-1][1]) % MOD)
