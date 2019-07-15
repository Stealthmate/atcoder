n, m, x = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
l = [t for t in a if t < x]
r = [t for t in a if t > x]
print(min(len(l), len(r)))
