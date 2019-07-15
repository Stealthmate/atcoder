s = input()
t = input()

for i in range(len(s)):
    r = s[i:] + s[:i]
    if r == t:
        print("Yes")
        exit(0)
print("No")
