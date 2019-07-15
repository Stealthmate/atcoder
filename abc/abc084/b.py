a, b = map(int, input().split(" "))
s = input()
p1 = s[:a]
m = s[a]
p2 = s[a+1:]
ans = ("-" not in p1) and ("-" not in p2) and (m == "-")
print("Yes" if ans else "No")
