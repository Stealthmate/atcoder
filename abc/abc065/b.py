n = int(input())
a = { (i + 1):int(input()) for i in range(n) }
s = 1
ans = 0
seen = set()
while True:
    if s == 2:
        break
    seen.add(s)
    s = a[s]
    ans += 1
    if s == 1 or s in seen:
        ans = -1
        break
print(ans)
