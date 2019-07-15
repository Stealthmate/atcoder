s = ''.join((reversed(input())))

while s:
    if s[0] in 'oku':
        s = s[1:]
    elif s[:2] == 'hc':
        s = s[2:]
    else:
        break
print("YES" if len(s) == 0 else "NO")
