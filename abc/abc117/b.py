n = int(input())
l = list(map(int, input().split(" ")))
ans = sum(l) - max(l) > max(l)
print("Yes" if ans else "No")
