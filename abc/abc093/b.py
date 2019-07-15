from itertools import chain
a, b, k = map(int, input().split(" "))
r1 = range(a, min(b + 1, a + k))
r2 = range(max(a, b - k + 1), b + 1)
ans = sorted(set((chain(r1, r2))))
print('\n'.join(str(x) for x in ans))
