import math
n = int(input())

r1 = 0
a = 0
rs = [int(input()) for i in range(n)]
rs.sort()
for i, r in enumerate(rs):
    if i % 2 == 1 - n % 2:
        a += math.pi * (r ** 2 - r1 ** 2)
    r1 = r
print(a)
