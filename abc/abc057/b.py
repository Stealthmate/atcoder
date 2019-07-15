n, m = map(int, input().split(" "))
ss = []
cs = []
for i in range(n):
    ss.append(list(map(int, input().split(" "))))
for i in range(m):
    cs.append(list(map(int, input().split(" "))))

for i in range(n):
    md = 0
    for j in range(m):
        d = abs(cs[j][0] - ss[i][0]) + abs(cs[j][1] - ss[i][1])
        if d < abs(cs[md][0] - ss[i][0]) + abs(cs[md][1] - ss[i][1]):
            md = j
    print(md + 1)
