k = int(input())

c = 1
j = 0
last_r = 1
for i in range(1, k + 1):
    if c % 10 == 0:
        c = 1
        j += 1
    n = int(str(c) + ("9" * j))
    r = n / sum(int(x) for x in str(n))

    if r < last_r:


    print(n)

    c += 1
