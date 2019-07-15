n = int(input())

t1 = 0
t2 = 0
t3 = 1
if n < 3:
    print(0)
elif n == 3:
    print(1)
else:
    for i in range(n - 3):
        t = t1 + t2 + t3
        t1 = t2
        t2 = t3
        t3 = t % 10007
    print(t3)
