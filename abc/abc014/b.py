n, X = map(int, input().split(" "))

ss = list(map(int, ("{:0" + str(n) + "b}").format(X)))
prices = map(int, input().split(" "))
print(sum([s * p for s,p in zip(reversed(ss), prices)]))
