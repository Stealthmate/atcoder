def binSearch(l, r, x, el):
    s = (l + r) // 2
    while x[s] != el:
        if r == l:
            return None
        s = (l + r) // 2
        if el < x[s]:
            r = (l + r) // 2
        else:
            l = (l + r) // 2 + 1
    return s

for d in range(1, 19):
    els =
