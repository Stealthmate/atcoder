a, b = map(int, input().split(" "))
c = int(str(a) + str(b))
i = 1
while i * i < c:
    i += 1
if i * i == c:
    print("Yes")
else:
    print("No")
