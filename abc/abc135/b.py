n = int(input())
p = list(map(int, input().split(" ")))

ps = sorted(p)

c = len([1 for x,y in zip(p, ps) if x != y])
if c == 2 or c == 0:
    print("YES")
else:
    print("NO")
