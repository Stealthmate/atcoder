# 解説を観てしまった、、、

from math import factorial
n = int(input())
xs = [int(input()) for i in range(n)]

ans = 0
for x in xs:
    dels = [y for y in xs if x % y == 0]
    dels.remove(x)

    e = 0
    if len(dels) == 0:
        e = 1
    elif len(dels) % 2 == 1:
        e = 1 / 2
    else:
        e = (len(dels) + 2) / (2*len(dels) + 2)
    ans += e
print(ans)
