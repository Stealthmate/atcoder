n = int(input())
a = [list(map(int, input().split(" "))) for i in range(n)]
print(sum(x[1] - x[0] + 1 for x in a))
