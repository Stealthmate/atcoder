n = int(input())
aas = map(int, input().split(" "))

m = 99999999999999999999
for a in aas:
    c = 0
    while a % 2 == 0:
        c += 1
        a = a // 2
    if c < m:
        m = c
print(m)
