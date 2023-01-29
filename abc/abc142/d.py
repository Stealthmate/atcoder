from fractions import gcd

a, b = map(int, input().split(" "))
x = gcd(a, b)

divs = {1: 1}

i = 2
while i * i <= x:
    if x % i == 0:
        divs[i] = 0
        x1 = x
        while x1 % i == 0:
            x1 = x1 // i
            divs[i] += 1
    i += 1
print(divs)
ans = 1
for d in divs.values():
    ans *= d
print(ans)
