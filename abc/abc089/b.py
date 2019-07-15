from collections import Counter
n = int(input())
a = list(input().split(" "))
ans = 'Y' in Counter(a).keys()
print("Four" if ans else "Three")
