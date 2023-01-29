n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

ans = 0
for i in range(n):
    x = b[i]
    x -= min(x, a[i])
    # print("Kill", b[i] - x, i)
    ans += b[i] - x
    if x > 0:
        y = min(x, a[i+1])
        # print("Kill", y, i + 1)
        ans += y
        x -= y
        a[i+1] -= y
print(ans)
