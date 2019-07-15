import math
n = int(input())

bugs = list(filter(lambda x: x > 0, map(int, input().split(" "))))
print(math.ceil(sum(bugs) / len(bugs)))
