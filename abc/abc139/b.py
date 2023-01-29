from math import log, ceil, floor

a, b = map(int, input().split(" "))

ans = 0
s = 1
while s < b:
    s += a - 1
    ans += 1
print(ans)
