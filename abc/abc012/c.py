n = int(input())

P = 2025

x = P - n

for i in range(1, 10):
    if x % i == 0:
        y = x / i
        if y < 10:
            print(i, "x", int(y))
