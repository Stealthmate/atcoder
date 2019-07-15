n, d = map(int, input().split(" "))
xs = set(tuple(map(int, input().split(" "))) for i in range(n))
ys = set(xs)
ans = 0
for x in xs:
    ys.remove(x)
    for y in ys:
        d2 = sum(abs(xx - yy) ** 2 for xx,yy in zip(x, y))
        j = 1
        while j ** 2 < d2:
            j += 1
        if j ** 2 == d2:
            ans += 1
print(ans)
