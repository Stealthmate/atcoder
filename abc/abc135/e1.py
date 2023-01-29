n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

s = sum(a)

for i in range(s, s * s + 1, s):
