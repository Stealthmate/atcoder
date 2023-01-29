from heapq import heappush, heappop

n, m = map(int, input().split(" "))
xys = [tuple(map(int, input().split(" "))) for i in range(n)]
xys = sorted(xys, key=lambda x: (x[0], -x[1]))

ans = 0

j = 0
h = []
for i in range(1, m + 1):
    while j < len(xys) and xys[j][0] <= i:
        heappush(h, -xys[j][1])
        j += 1
    if h:
        x = -heappop(h)
        # print("Pick", x)
        ans += x

print(ans)
