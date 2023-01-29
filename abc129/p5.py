L = int(input())

groupsWithN = []

for i in range(1, len(L) - 1):
    groupsWithN.append(3*groupsWithN[i - 1])
