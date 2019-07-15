from collections import Counter
n = int(input())
ns = [input() for i in range(n)]
m = int(input())
ms = [input() for i in range(m)]
cn = dict(Counter(ns).most_common())
cm = dict(Counter(ms).most_common())
for i in cn.keys():
    cn[i] -= cm[i] if i in cm else 0
print(max(sorted(cn.values(), reverse=True)[0], 0))
