input()
fs = list(map(int, input().split(" ")))

def hb(x1):
    x = x1
    if x % 2 == 0:
        x -= 1
    if x % 3 == 2:
        x -= 2
    return x1 - x
print(sum(hb(x) for x in fs))
