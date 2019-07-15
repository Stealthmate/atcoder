a, b, c = map(int, input().split(" "))

isA = a + b == c
isB = a - b == c

if isA and isB:
    print("?")
elif isA:
    print("+")
elif isB:
    print("-")
else:
    print("!")
