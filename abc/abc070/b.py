a, c, b, d = map(int, input().split(" "))
print(max(0, min(c, d) - max(a, b)))
