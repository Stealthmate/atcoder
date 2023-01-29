n = int(input())
s = [list(input()) for i in range(n)]

def works(a, b):
    ans = True
    def x(xx):
        return (xx + a) % n
    def y(yy):
        return (yy + b) % n

    for i in range(n):
        for j in range(i, n):
            ans = ans and (s[x(i)][y(j)] == s[x(j)][y(i)])

    return ans

ans = n * int(works(0, 0))
for i in range(1, n):
    ans += (n - i) * works(i, 0)
    ans += (n - i) * works(0, i)

print(ans)
