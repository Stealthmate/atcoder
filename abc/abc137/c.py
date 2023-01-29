from collections import Counter

n = int(input())
ss = [''.join(sorted(input())) for i in range(n)]
cs = Counter(ss)
ans = 0
for c in cs.most_common():
    if c[1] > 1:
        ans += c[1] * (c[1] - 1) // 2
print(ans)
