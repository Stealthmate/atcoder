n = int(input())

a = n // 100
if n <= int(str(a) * 3):
    print(str(a) * 3)
else:
    print(str(a + 1) * 3)
