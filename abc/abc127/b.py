r, d, x = map(int, input().split(" "))
s = x
for i in range(10):
    s = r*s - d
    print(s)
