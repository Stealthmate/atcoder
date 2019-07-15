n = int(input())

if n == 1:
    print(0)
    exit(0)

i = 1
lastMin = 999999999999
while i ** 2 <= n:
    a = i
    b = n // i
    m = abs(a - b) + n - (a * b)
    if m < lastMin:
        lastMin = m
    i += 1

print(lastMin)
