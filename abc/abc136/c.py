n = int(input())
hs = list(map(int, input().split(" ")))

ans = True
m = -1
for i in range(0, n):
    if hs[i] > m:
        m = hs[i]
    elif m - hs[i] > 1:
        ans = False
        break
print("Yes" if ans else "No")
