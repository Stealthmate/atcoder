s = input()

l = 0
current = 'R'
ans = [0 for x in s]
for i,c in enumerate(s):
    if c == current:
        l += 1
    elif l > 0:
        for j in range(l):
            ans[i - 1] += j % 2 == 0
            ans[i] += j % 2 == 1
        l = 0

l = 0
current = 'L'
for i,c in enumerate(reversed(s)):
    if c == current:
        l += 1
    elif l > 0:
        for j in range(l):
            ans[-i] += j % 2 == 0
            ans[-(i + 1)] += j % 2 == 1
        l = 0

print(' '.join(str(x) for x in ans))
