l, h = map(int, input().split(" "))
n = int(input())
a = [int(input()) for i in range(n)]

for i in a:
    if i > h:
        print(-1)
    elif i >= l:
        print(0)
    else:
        print(l - i)
