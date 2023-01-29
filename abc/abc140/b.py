n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))

a = [x-1 for x in a]

ans = 0

prev = None
for i in a:
    ans += b[i]
    if prev is not None and prev == i - 1:
        ans += c[i - 1]
    prev = i
print(ans)
