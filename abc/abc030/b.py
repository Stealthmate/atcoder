n, m = map(int, input().split(" "))

a2 = 360 * m / 60
a1 = 360 * (n % 12) / 12 + (a2 / 12)
print(min(abs(a1 - a2), 360 - abs(a1 - a2)))
