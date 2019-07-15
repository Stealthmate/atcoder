n = int(input())

cs = []
for i in range(n):
    m, p = input().split(" ")
    p = int(p)
    cs.append((m, p))

top = max(cs, key=lambda x: x[1])
total = sum([x[1] for x in cs])
if top[1] > total / 2:
    print(top[0])
else:
    print("atcoder")
