M, K = map(int, input().split(" "))

if (M, K) == (1, 0):
    print("0 0 1 1")
elif K > (2 ** M) - 1 or (M, K) == (1, 1):
    print(-1)
else:
    elems = list(x for x in range(2 ** M) if x != K)
    print(' '.join(str(x) for x in elems), K, ' '.join(str(x) for x in reversed(elems)), K)
