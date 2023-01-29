k, x = map(int, input().split(" "))
for i in range(max(x - k + 1, -1000000), min(x + k, 1000001)):
    print(i, end=' ')
print()
