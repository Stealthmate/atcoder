n, k = map(int, input().split(" "))
s = list(map(int, input().split(" ")))

ans = 0
for i in range(n - 1):
    if i == 0:
        if s[i] == 'R' and s[i+1] == 'R':
            ans += 1
    elif i == n - 2:
        if s[i] == 'L' and s[i + 1] == 'L':
            ans += 1
    elif s[i] == s[i + 1] and s[i]:
        ans += 1

while True:
    start = None
    end = None
    for i in range(n):
        if i == 0:
            if s[i] == 'L':
                start = i
        elif i == n - 1:
            if s[i] == 'R' and s[i-1] == 'L'
