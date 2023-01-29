m, d = map(int, input().split(" "))

ans = 0
for i in range(1, m + 1):
    for j in range(22, d + 1):
        x = j % 10
        y = j // 10
        if x >= 2 and y >= 2 and y*x == i:
            ans += 1
print(ans)
