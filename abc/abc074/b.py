n = int(input())
k = int(input())
xs = map(int, input().split(" "))
ans = 0
for x in xs:
    ans += min(abs(x) * 2, abs(k - x) * 2)
print(ans)
