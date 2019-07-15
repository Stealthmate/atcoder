x = int(input())

ans = 1
k = 2
while 2 ** k <= x:
    # print("k =", k)
    i = 1
    while i ** k <= x:
        # print("i =", i)
        r = i ** k
        # print("r =", r)
        ans = max(ans, r)
        i += 1
    k += 1
print(ans)
