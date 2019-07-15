n, q = map(int, input().split(" "))

arr = [0] * n
for i in range(q):
    l, r, t = map(int, input().split(" "))
    for j in range(l - 1, r):
        arr[j] = t
print("\n".join(str(x) for x in arr))
