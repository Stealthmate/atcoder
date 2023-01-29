N = int(input())
coins = [0, 0, 0, 0, 0, 0]
# coins = [0, 0, 0]
for i in range(len(coins)):
    coins[i] = int(input())
COIN = [500, 100, 50, 10, 5, 1]
# COIN = [500, 100, 50]

ways = [(0, [0 for _ in COIN]) for i in range(N)]





for i in range(1, N):
    for c in COIN:
        if i >= c:
            p1,req1 = ways[i - c]
            p2,req2 = ways[c]
            p3, req3 = 0, [0 for _ in COIN]
            # print(i, c)
            if i == c and coins[COIN.index(c)] > 0:
                p3, req3 = 1, [1 if ci == i else 0 for ci in COIN]
            req = [max(a + b, d) for a,b,d in zip(req1, req2, req3)]
            if all([ x < y for x,y in zip(req, coins)]):
                print("Can make", i, "with", req)
                ways[i] = p1 + p2 + p3, req

print(ways[N-1])
            
