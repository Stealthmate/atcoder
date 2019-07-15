n = int(input())
t, a = map(int, input().split(" "))
hs = list(map(int, input().split(" ")))
hs = [ abs(a - (t - h * 0.006)) for h in hs ]
print(hs.index(min(hs)) + 1)
