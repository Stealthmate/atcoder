s = input()
n = int(input())
lrs = [(int(x) for x in input().split(" ")) for i in range(n)]
for l,r in lrs:
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]

print(s)
