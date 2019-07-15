from collections import Counter
n = int(input())
m = (1, 0)
for i in range(1, n+1):
    j = 0
    ii = i
    while ii % 2 == 0:
        ii /= 2
        j += 1
    if m[1] < j:
        m = (i, j)
print(m[0])
