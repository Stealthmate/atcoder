from collections import Counter
s = input()
ans = Counter(s).most_common()
ans = all(map(lambda x: x[1] % 2 == 0, ans))
print("Yes" if ans else "No")
