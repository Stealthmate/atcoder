n, a, b = map(int, input().split(" "))

p = 0
for i in range(n):
    s, d = input().split(" ")
    d = int(d)
    s = 1 if s == 'East' else -1

    p += s * max(a, min(d, b))

if p > 0:
    print("East", p)
elif p < 0:
    print("West", -p)
else:
    print(0)
