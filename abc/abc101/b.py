n = input()
ans = int(n) % sum(map(int, n)) == 0
print("Yes" if ans else "No")
