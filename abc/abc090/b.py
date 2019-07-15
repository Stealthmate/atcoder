a, b = list(map(int, input().split(" ")))
ans = 0
for i in range(a, b + 1):
    s = str(i)
    ans += s[:2] == s[3:][::-1]
print(ans)
