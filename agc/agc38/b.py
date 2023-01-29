import bisect

n, k = map(int, input().split(" "))
p = list(map(int, input().split(" ")))

ans = int(sorted(p) == p) if k == n else int(sorted(p[:k]) != p[:k])
hasSame = False
for i in range(k + 1, n + 1):
    frame = sorted(p[i - k:i])

    a = p[i-k-1]
    x_a = bisect.bisect_left(frame, a)
    x_e = bisect.bisect_left(frame, p[i - 1])

    areSame = all(x == y for x, y in zip(frame, p[i-k:i]))
    # print(frame, p[i-k:i], x_a, a, x_e)
    if areSame and not hasSame:
        # print("First same")
        # print(p[:i-k] + frame + p[i:])
        ans += 1
        hasSame = True
        continue

    if x_a == 0 and x_e == k - 1:
        # print("A first E last", a)
        pass
    elif x_a > 0 and areSame:
        # print("A nonfirst, same")
        pass
    else:
        # print("Good")
        # print(p[:i-k] + frame + p[i:])
        ans += 1

    frame.

print(ans)
