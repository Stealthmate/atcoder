n, k = map(int, input().split(" "))
qs = [list(map(int, input().split(" "))) for i in range(n)]


def find(x, i):
    for q in qs[i]:
        p = x ^ q
        if i < len(qs) - 1 and find(p, i + 1):
            return True
        if p == 0:
            return True
    return False

print("Found" if find(0, 0) else "Nothing")
