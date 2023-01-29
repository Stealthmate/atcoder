n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

ans = 0
for i, ai in enumerate(a):
    left = 0
    right = 0
    for j in range(i):
        if ai > a[j]:
            left += 1
    for j in range(i + 1, n):
        if ai > a[j]:
            right += 1
    ans += (k * (k + 1) * right // 2) + (k * (k - 1) * left // 2)
print(ans % 1000000007)
