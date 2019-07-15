n, k = map(int, input().split(" "))
ls = sorted(map(int, input().split(" ")))
print(sum(reversed(ls[n-k:])))
