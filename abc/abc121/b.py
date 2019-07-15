n, m, c = map(int, input().split(" "))
b = list(map(int, input().split(" ")))
a = [list(map(int, input().split(" "))) for i in range(n)]
ans = len([x for x in a if sum([x[i] * b[i] for i in range(m)]) + c > 0])
print(ans)
