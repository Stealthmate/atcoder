from collections import Counter
n = int(input())
a, b = map(int, input().split(" "))
k = int(input())
ps = [a, b]
ps.extend(map(int, input().split(" ")))
if Counter(ps).most_common()[0][1] > 1:
    print("NO")
else:
    print("YES")
