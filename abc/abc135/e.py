K = int(input())
X, Y = map(int, input().split(" "))

seen = set()
route = []

p = (0, 0)

while p not in seen and p != (X, Y):
    seen.add(p)
    print(p)
    route.append(p)
    dx = X - p[0]
    if abs(dx) > K:
        dx = (dx // abs(dx)) * K
    dy = Y - p[1]
    dy = (dy // abs(dy)) * (K - abs(dx))
    print("Go", dx, dy)
    p = (p[0] + dx, p[1] + dy)
if p == (X, Y):
    print("\n".join(str(x) + " " + str(y) for x, y in route))
    print(X, Y)
else:
    print(-1)
