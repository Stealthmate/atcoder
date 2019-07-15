n, t = map(int, input().split(" "))
c = [tuple(map(int, input().split(" "))) for i in range(n)]
c = [x for x in c if x[1] <= t]
if c:
    print(min(c)[0])
else:
    print("TLE")
