from collections import Counter

n, k = map(int, input().split(" "))
s = input()

ans = ""
diff = 0
T = sorted(s)
i = 0
while T:
    for j, t in enumerate(T):
        tmp = ans + t
        tmp_diff = diff + (s[i] != t)
        Tt = list(T)
        Tt.pop(j)
        c = Counter(s[i+1:])
        ct = Counter(Tt)
        if sum(max(Tt.count(u) - s[i+1:].count(u), 0) for u in list(set(Tt))) + tmp_diff <= k:
            ans = tmp
            diff = tmp_diff
            T.pop(j)
            i += 1
            break
print(ans)
