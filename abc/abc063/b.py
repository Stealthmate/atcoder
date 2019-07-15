from collections import Counter
s = input()
ans = len(Counter(s).most_common()) == len(s)
print("yes" if ans else "no")
