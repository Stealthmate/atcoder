W, a, b = map(int, input().split(" "))
if a <= b <= a + W or b <= a <= b + W:
    print(0)
else:
    print(min(abs(a + W - b), abs(b + W - a)))
