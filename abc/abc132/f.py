N, K = map(int, input().split(" "))

LIM = int(N ** 0.5) * 2 + 1
dp = [[0] * LIM for i in range(K - 1)]

ts = set()
tsl = []
tsr = []
num = {}
for i in range(1, int(N ** 0.5) + 1):
    x = N // i
    y = N // (N // i)
    if not tsl or tsl[-1] > x:
        tsl.append(x)
    if x != y and (not tsr or tsr[-1] < y):
        tsr.append(y)
    if x not in num:
        num[x] = 0
    if y not in num:
        num[y] = 0
ts = tsl + tsr[::-1]

idx = {k: i for i, k in enumerate(ts)}
for j, t in enumerate(ts):
    num[t] = (N // t - N // ts[j-1]) if j > 0 else 1
    # print(t, num[t])
    dp[0][idx[t]] = num[t] * t


MOD = 1000000007
for i in range(1, K - 1):
    pref = 0
    for j in reversed(range(len(ts))):
        # R = idx[N // ts[j]]
        R = len(ts) - j - 1
        pref += dp[i-1][R]
        dp[i][j] = pref * num[ts[j]] % MOD
        # pref += dp[i-1][R] * num[ts[j]]

        # print(f"0 - {R}")
        # dp[i][j] = sum(dp[i-1][k] * num[ts[j]] for k in range(R + 1))
        # print(pref, dp[i][j])


# for x in dp:
    # print(x)
ans = sum(dp[-1])
print(ans % 1000000007)
