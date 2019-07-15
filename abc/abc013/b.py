a = int(input())
b = int(input())

print(min([abs(a - b), 10 - a + b, 10 - b + a]))
