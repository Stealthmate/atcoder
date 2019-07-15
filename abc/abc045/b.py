ss = [input() for i in range(3)]

p = 0
while len(ss[p]) > 0:
    c = ss[p][0]
    ss[p] = ss[p][1:]
    p = {'a': 0, 'b': 1, 'c': 2}[c]
print("ABC"[p])
