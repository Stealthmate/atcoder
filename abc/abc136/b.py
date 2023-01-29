n = int(input())

s = len(str(n))


ans = n - (10 ** (s - 1) - 1) if s % 2 == 1 else 0
for i in range(1, s, 2):
    ans += 10 ** i - 10 ** (i - 1)
print(ans)
