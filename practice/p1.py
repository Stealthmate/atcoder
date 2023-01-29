from collections import deque
from copy import copy

L, N = [int(x) for x in input().split(" ")]
X = deque([int(input()) for x in range(N)])

def calc(X, p, t):
    pos = p
    total = t
    while X:
        if pos < X[0]:
            total += L - X[-1] + pos
            pos = X.pop()
        else:
            total += X[0] + L - pos
            pos = X.popleft()
    return total

X1 = copy(X)
p1 = X1.popleft()
t1 = p1
X2 = copy(X)
p2 = X2.pop()
t2 = L - p2
print(max(calc(X1, p1, t1), calc(X2, p2, t2)))
