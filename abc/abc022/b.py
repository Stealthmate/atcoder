from collections import Counter

n = int(input())
ps = []
for i in range(n):
    ps.append(int(input()))

print(sum([x[1] - 1 for x in Counter(ps).most_common() if x[1] > 1]))
