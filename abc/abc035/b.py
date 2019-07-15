from collections import Counter

s = input()
t = int(input())

ds = {
    'U': 1,
    'D': -1,
    'L': -1,
    'R': 1
}

d = abs(sum([ds[x] for x in s if x in 'UD'])) + abs(sum([ds[x] for x in s if x in 'LR']))

q = len([x for x in s if x == '?'])

if t == 1:
    print(d + q)
else:
    dd = min(q, d)
    print(d - dd + ((q - dd) % 2))
