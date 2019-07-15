s = input()

for i in reversed(range(2, len(s), 2)):
    m = i//2
    if s[:m] == s[m:i]:
        print(i)
        exit(0)
