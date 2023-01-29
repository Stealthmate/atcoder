n, m = map(int, input().split(" "))

X = -1
Y = -1
Z = -1
for i in range(0, n + 1):
    y = m - 2*n - 2*i
    x = n - y - i
    if min(x, y, i) >= 0 and max(x, y, i) > 0:
        X = x
        Y = y
        Z = i
        break
print(X, Y, Z)
