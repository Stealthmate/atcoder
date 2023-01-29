from math import sqrt
import numpy as np

s = int(input())

def fact(x):
    i = 2
    while i ** 2 <= x:
        if x % i == 0:
            return i
        i += 1
    return None

facts = []
x = s
LIM = 10 ** 9
while x > LIM:
    print("Fact", x)
    f = fact(x)
    if f == None:
        break
    facts.append((x, f))
    x = x // f
# print(facts)
print(x, s // x)
