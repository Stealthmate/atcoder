n = int(input())

ans = int(n >= 105)
for i in range(107, n + 1, 2):
    dc = 0
    for j in range(1, i // 2):
        if i % j == 0:
            dc += 1
    if dc == 7:
        ans += 1
print(ans)
