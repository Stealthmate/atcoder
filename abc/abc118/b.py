n, m = map(int, input().split(" "))
ks = [set(list(map(int, input().split(" ")))[1:]) for i in range(n)]
ans = set.intersection(*ks)
print(len(ans))
