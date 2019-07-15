# https://pyteyon.hatenablog.com/entry/2019/01/03/200534
# ここで解説調べた

n = int(input())
a = list(map(int, input().split(" ")))

if(sum(a) % n != 0):
    print(-1)
    exit(0)

p = sum(a) / n
nb = 0
cs = 0
last = 0
for i, s in enumerate(a):
    cs += p - s
    if cs == 0:
        nb += i - last
        last = i + 1

print(nb)
