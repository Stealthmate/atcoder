h, w = map(int, input().split(" "))
ss = [list(input()) for i in range(h)]

def hb(i, j):
    b = ss[i][j] == '#'
    if j > 0:
        b += ss[i][j-1] == '#'
    if j < w - 1:
        b += ss[i][j+1] == '#'
    return b

for i in range(h):
    for j in range(w):
        if ss[i][j] == '#':
            continue

        b = 0
        if i > 0:
            b += hb(i-1, j)
        b += hb(i, j)
        if i < h - 1:
            b += hb(i+1, j)
        ss[i][j] = chr(ord('0') + b)
print('\n'.join(''.join(s) for s in ss))
