from math import ceil
n, h = map(int, input().split(" "))
a, b, c, d, e = map(int, input().split(" "))

ans = 9999999999999999999

bigIsBetter = b / a > d / c

for i in range(n + 1):
    needed = h - i*e
    if needed == 0:
        needed = -1
    needed = -min(h - i*e - 1, 0)
    m = n - i
    if needed == 0:
        ans = min(ans, m * c)
    elif needed > m * b:
        break
    else:
        # print("Needed")
        k = ceil(max(needed - (m * d), 0) / (b - d))
        # print("Eat", k, "big and", m - k, "small")
        ans = min(ans, k*a + (m - k) * c)

print(ans)
