n = int(input())

ans = n % 4 == 0
if not ans:
    for i in range(n // 4):
        if (n - i*4) % 7 == 0:
            ans = True
            break
print("Yes" if ans else "No")
