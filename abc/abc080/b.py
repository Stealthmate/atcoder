n = int(input())
n1 = sum(map(int, str(n)))
print("Yes" if n % n1 == 0 else "No")
