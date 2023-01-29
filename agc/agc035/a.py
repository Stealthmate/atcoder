from collections import Counter
n = int(input())
a = list(map(int, input().split(" ")))

# ans = False
# x = a[0]
# y = a[1]
# available = list(a[2:])
# while available:
#     r = x ^ y
#     if r in available:
#         available.remove(r)
#         x = y
#         y = r
#     else:
#         break
# if not available:
#     ans = x ^ y == a[0]

# print("Yes" if ans else "No")

c = Counter(a).most_common()
if len(c) == 3 and c[0][0] ^ c[1][0] == c[2][0] and c[0][1] == c[1][1] and c[1][1] == c[2][1]:
    ans = True
elif len(c) == 2 and c[0][0] ^ c[1][0] == c[0][0] and (c[0][1] * 2 == c[1][1] or c[0][1] == c[1][1] * 2):
    ans = True
elif len(c) == 1 and c[0][0] == 0:
    ans = True
else:
    ans = False
print("Yes" if ans else "No")
