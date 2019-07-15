n = int(input())
d, x = map(int, input().split(" "))
a = [int(input()) for i in range(n)]

ans = x
for ai in a:
    k = 1 + ((d - 1) // ai)
    ans += k
print(ans)
