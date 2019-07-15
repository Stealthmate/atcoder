n = int(input())
ts = list(map(int, input().split(" ")))
m = int(input())
total = sum(ts)
for i in range(m):
    p, x = map(int, input().split(" "))
    print(total - ts[p - 1] + x)
