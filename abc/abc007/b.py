s = input()
if len(s) == 1 and s[0] == 'a':
    print(-1)
elif len(s) == 1:
    print(chr(ord(s[0]) - 1))
else:
    print(s[:-1])
