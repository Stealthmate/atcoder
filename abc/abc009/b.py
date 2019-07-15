n = int(input())
arr = list(set(int(input()) for i in range(n)))
arr.sort()
print(arr[-2])
