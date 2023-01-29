s = input()
t = input()
print(len([x for x, y in zip(s, t) if x == y]))
