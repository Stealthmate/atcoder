from math import ceil
ds = [int(input()) for i in range(5)]
t = sum(10 * ceil(x / 10) for x in ds)
rs = [x % 10 for x in ds if x % 10 != 0]
r = (min(rs) - 10) if rs else 0
print(t + r)
