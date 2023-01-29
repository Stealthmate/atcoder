n, k = map(int, input().split(" "))
hs = list(map(int, input().split(" ")))

print(len([x for x in hs if x >= k]))
