n = int(input())
h = list(map(int, input().split(" ")))

ans = 0
c = 0
for i in range(1, n):
    if h[i-1] < h[i]:
        ans = max(ans, c)
        c = 0
    else:
        c += 1
ans = max(c, ans)
print(ans)
