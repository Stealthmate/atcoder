a, b, c = map(int, input().split(" "))

r1 = a % b
r0 = c % b

r = r1
while True:
    if r == r0:
        print("YES")
        break
    r = (r + r1) % b
    if r == r1:
        print("NO")
        break
