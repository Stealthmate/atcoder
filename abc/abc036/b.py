n = int(input())
ss = [input() for i in range(n)]

for i in range(n):
    for j in reversed(range(n)):
        print(ss[j][i], end='')
    print()
