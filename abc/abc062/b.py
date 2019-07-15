h, w = map(int, input().split(" "))
a = [input() for i in range(h)]
print("#" * (w + 2))
for s in a:
    print("#" + s + "#")
print("#" * (w + 2))
