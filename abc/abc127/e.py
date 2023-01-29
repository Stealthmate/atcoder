from math import factorial

N, M, K = map(int, input().split(" "))

all_nodes = [(x, y) for x in range(N) for y in range(M)]
total = 0
for i in range(len(all_nodes)):
    for j in range(i + 1, len(all_nodes)):
        total += abs(all_nodes[i][0] - all_nodes[j][0]) + abs(all_nodes[i][1] - all_nodes[j][1])

X = (N * M)
X = X * (X - 1) // 2
Y = K * (K - 1) // 2
# print(X)
# print(Y)
f1 = factorial(X - 1)
f2 = factorial(Y - 1)
f3 = factorial(X - Y)
# print(f1)
# print(f2)
# print(f3)
ans = f1 // (f2 * f3)
MOD = 1000000007
print((ans * total) % MOD)
