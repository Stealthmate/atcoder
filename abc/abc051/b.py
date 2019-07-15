k, n = map(int, input().split(" "))

ans = 0
for i in reversed(range(k + 1)):
    start = min(k, n - i)
    if n - i - start > k:
        continue
    for j in reversed(range(start + 1)):
        if(n - i - j <= k):
            # print(i, j, n - i - j)
            ans += 1

print(ans)
