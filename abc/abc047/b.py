w, h, n = map(int, input().split(" "))
xyas = [map(int, input().split(" ")) for i in range(n)]

X = 0
X1 = w
Y = 0
Y1 = h
for x, y, a in xyas:
    if a == 1:
        X = max(X, x)
        X1 = max(X1, x)
    elif a == 2:
        X = min(X, x)
        X1 = min(X1, x)
    elif a == 3:
        Y = max(Y, y)
        Y1 = max(Y1, y)
    else:
        Y = min(Y, y)
        Y1 = min(Y1, y)

print(abs(X - X1) * abs(Y - Y1))
