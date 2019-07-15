s = set(input())
s1 = set("abcdefghijklmnopqrstuvwxyz")
ans = sorted(list(s1 - s))
if ans:
    print(ans[0])
else:
    print("None")
