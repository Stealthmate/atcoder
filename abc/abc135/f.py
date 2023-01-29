from math import ceil
import re

s = input()
t = input()

N = len(s)
M = len(t)

def matches1(S, W):
    S = S * ceil(M / N)
    print(S)
    print(W)

    def kmp_table():
        T = [0] * (len(W) + 1)

        T[0] = -1
        pos = 1
        cnd = 0
        while pos < len(W):
            print(pos, cnd)
            if W[pos] == W[cnd]:
                T[pos] = T[cnd]
            else:
                T[pos] = cnd
                cnd = T[cnd]
                while cnd >= 0 and W[pos] != W[cnd]:
                    cnd = T[cnd]
                pos += 1
            cnd += 1
        T[pos] = cnd

        return T

    P = [False for x in S]
    j = 0
    k = 0
    T = kmp_table()

    while j < len(S):
        if W[k] == S[j]:
            j += 1
            k += 1
            if k == len(W):
                P[j - k] = True
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1

    return P

# def matches(S, T, i):
#     M = len(T)
#     for j in range(len(T)):
#         if S[(i + j) % N] != T[j]:
#             return False
#     return True

start = 0
i = 0
count = 0
ans = 0
breaks = set()
# matches = [matches(s, t, i) for i in range(N)]
matches = matches1(s, t)
paths = [None for x in range(N)]
currentPath = []
# print(matches)
for i in range(N):
    start = i
    l = 0
    # print("Start", i)
    while matches[start]:
        # print(start)
        if start in currentPath:
            print(-1)
            exit(0)
        if paths[start] is not None:
            l += paths[start]
            break

        currentPath.append(start)
        l += 1
        start = (start + M) % N

    for j, x in enumerate(currentPath):
        paths[x] = l - j

    currentPath = []

paths = paths + [0]
# print(paths)
print(max(p for p in paths if p is not None))
