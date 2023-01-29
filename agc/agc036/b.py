n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

s = []
i = 0
while i < n * k:
    r = i % n
    if r == 0 and s == [] and i != 0:
        i = i * (n * k // i)
    x = a[r]
    j = 0
    try:
        seq = list(a)
        if i // n < k - 1:
            seq.extend(a)
        j = seq[r+1:].index(x)
        i = i + j + 2
    except:
        s.append(a[r])
        i += 1
print(' '.join(str(y) for y in s))
