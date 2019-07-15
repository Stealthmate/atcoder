a, b, c, x = [int(input()) for i in range(4)]

ans = 0
for i in range(0, min(a + 1, (x // 500) + 1)):
    start = min(500 * i, x)
    for j in range(0, min(b + 1, ((x - start) // 100) + 1)):
        start1 = min(start + j * 100, x)
        left = x - start1
        if left // 50 <= c:
            ans += 1
print(ans)
