n = int(input())
s = input()

ans = 0
for i in range(len(s)):
    ans = max(ans, len(set(s[:i+1]) & set(s[i+1:])))
print(ans)
