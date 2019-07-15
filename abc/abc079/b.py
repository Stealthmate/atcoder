n = int(input())
l1 = 2
l2 = 1
for i in range(1, n):
    l3 = l1 + l2
    l1 = l2
    l2 = l3
print(l2)
