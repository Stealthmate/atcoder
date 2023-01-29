from collections import deque

N, A, B, C, D = map(int, input().split(" "))
A -= 1
B -= 1
C -= 1
D -= 1
S = input()

s = deque()
s.append((A, B))
r = False

def canMove(f, step, o):
    return f + step < len(S) and f + step != o and S[f + step] == '.'

canGo = {}

while s:
    a, b = s.pop()
    if (a, b) in canGo:
        continue

    # SS = list(S)
    # SS[a] = 'A'
    # SS[b] = 'B'
    # print(''.join(SS))
    if a == C and b == D:
        r = True
        break

    if b < D:
        can1 = canMove(b, 1, a)
        can2 = canMove(b, 2, a)
        if not can1 and not can2 and a == C:
            # print("Can go no more", a, b, ''.join(SS))
            canGo[(a, b)] = False
            continue

        if b + 1 <= D and can1 and (a, b + 1) not in canGo:
            s.append((a, b + 1))
            can = True
        if b + 2 <= D and can2 and (a, b + 2) not in canGo:
            s.append((a, b + 2))
            can = True
        if not can:
            canGo[(a, b)] = False
            continue

    if a < C:
        can1 = canMove(a, 1, b)
        can2 = canMove(a, 2, b)
        if not can1 and not can2 and b == D:
            # print("Can go no more", a, b, ''.join(SS))
            canGo[(a, b)] = False
            continue

        can = False
        if a + 1 <= C and can1 and (a + 1, b) not in canGo:
            s.append((a + 1, b))
            can = True
        if a + 2 <= C and can2 and (a + 2, b) not in canGo:
            s.append((a + 2, b))
            can = True
        if not can:
            canGo[(a, b)] = False
            continue

if r:
    print("Yes")
else:
    print("No")
