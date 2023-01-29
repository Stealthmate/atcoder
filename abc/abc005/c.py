t = int(input())
n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
b = list(map(int, input().split(" ")))

a.sort()
b.sort()

def doIt():
    for i in b:
        can = False
        for j in a:
            if j <= i and i - j <= t:
                can = True
                a.remove(j)
                break
        if not can:
            return False
    return True

print("yes" if doIt() else "no")
