n = int(input())
ws = list(map(int, input().split(" ")))
s1 = 0
s2 = sum(ws)
md = 9999999999999999999999999999
for w in ws:
    s1 += w
    s2 -= w
    if abs(s1 - s2) < md:
        md = abs(s1 - s2)
print(md)
