n = int(input())
s = input()

if(len(s) % 2 == 0):
    print(-1)
    exit(0)

mid = len(s) // 2
i = 0

step = 2
count = 0
while i < mid:
    x = s[mid - i]
    y = s[mid + i]
    if (step == 0 and x == 'a' and y == 'c') or (step == 1 and x == 'c' and y == 'a') or (step == 2 and x == 'b' and y == 'b'):
        step = (step + 1) % 3
        count += 1
        i += 1
    else:
        count = -1
        break

print(count)
