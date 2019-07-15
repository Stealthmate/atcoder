s = input()
current = s[0]
count = 1
ans = ''
for c in s[1:]:
    if current != c:
        ans = '{}{}{}'.format(ans, current, count)
        current = c
        count = 1
    else:
        count += 1
ans = '{}{}{}'.format(ans, current, count)
print(ans)
