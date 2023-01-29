from math import sqrt

txa, tya, txb, tyb, T, V = map(int, input().split(" "))
n = int(input())
xys = [tuple(map(int, input().split(" "))) for i in range(n)]

md = T * V

def dist(a, b):
    return sqrt(abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2)

a = (txa, tya)
b = (txb, tyb)
for c in xys:
    d = dist(a, c) + dist(c, b)
    if d <= md:
        print("YES")
        exit(0)
print("NO")
