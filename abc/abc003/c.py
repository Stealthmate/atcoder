n, k = map(int, input().split(" "))
r = list(map(int, input().split(" ")))
r.sort()
rt = 0
for rr in r[n-k:]:
    rt = (rt + rr) / 2
print(rt)
