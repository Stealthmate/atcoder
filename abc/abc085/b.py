from collections import Counter
n = int(input())
d = [int(input()) for i in range(n)]
print(len(Counter(d).keys()))
