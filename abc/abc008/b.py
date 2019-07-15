from collections import Counter
n = int(input())
ss = [input() for i in range(n)]
print(Counter(ss).most_common()[0][0])
