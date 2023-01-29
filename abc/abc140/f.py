import bisect

n = int(input())
s = list(map(int, input().split(" ")))
# n = 18
# s = list(reversed(range(1, 2 ** n + 1)))

s = sorted(s)
from collections import deque

def solve():
    global s

    parents = [s[-1]]
    s.pop()

    for i in range(n):
        newparents = list(parents)
        k = len(s)
        dropped = set()
        # print(parents)
        for p in parents:
            oldK = k
            k = bisect.bisect(s, p - 1, 0, k) - 1
            # print("Old", oldK, k, s[k], p)
            if k == -1:
                print("No")
                exit(0)

            newparents.append(s[k])
            dropped.add(k)
        s = [x for i, x in enumerate(s) if i not in dropped]
        parents = sorted(newparents, reverse=True)

    # print(parents)
    # print(k)
    if k == len(s):
        print("Yes")
    else:
        print("No")
solve()
