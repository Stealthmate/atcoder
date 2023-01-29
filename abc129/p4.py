from collections import namedtuple
from itertools import chain

h, w = map(int, input().split(" "))

def neighbours(n):
    return sum(n)

nodes = []
lastUp = [0] * w
lastLeft = 0
for i in range(h):
    lastLeft = 0
    nodes.append([])
    for j,c in enumerate(input()):
        good = 1 if c == '.' else 0
        left = 0
        up = 0
        right = w - j - 1
        down = h - i - 1
        if good == 1:
            if j > 0:
                l = nodes[i][j - 1]
                left = l[1] + l[0]
            if i > 0:
                u = nodes[i - 1][j]
                up = u[2] + u[0]
        else:
            right = 0
            down = 0
            for k in range(lastLeft, j):
                nodes[i][k][3] = j - k - 1
            for k in range(lastUp[j], i):
                nodes[k][j][4] = i - k - 1
            lastLeft = j + 1
            lastUp[j] = i + 1
        nodes[i].append([good, left, up, right, down])

mx = -1
for i in range(h):
    for j in range(w):
        n = neighbours(nodes[i][j])
        if n > mx:
            mx = n

print(mx)
