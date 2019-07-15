n, m = map(int, input().split(" "))

i1 = [ input() for i in range(n) ]
i2 = [ input() for i in range(m) ]

for i in range(0, n - m + 1):
    for j in range(0, n - m + 1):
        si = [ x[j:j + m] for x in i1[i:i + m] ]
        if si == i2:
            print("Yes")
            exit(0)
print("No")
