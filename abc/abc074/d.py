n = int(input())
a = [list(map(int, input().split(" "))) for i in range(n)]

ans = 0

class Found(Exception):
    pass
class BadAns(Exception):
    pass

def dijk(s, t):
    dist = { k: 9999999999999 for k in range(n) }
    pred = { k: None for k in range(n) }
    Q = set(range(n))

    dist[s] = 0
    pred[s] = None

    try:
        while Q:
            node = min([x for x in dist.items() if x[0] in Q], key=lambda x: x[1])[0]
            # print("Traverse", node)
            try:
                Q.remove(node)
            except KeyError:
                raise Found

            for nei, sdist in enumerate(a[node]):
                if nei == t and node == s or node == nei:
                    # print("SKIP", node, nei)
                    pass
                else:
                    alt = dist[node] + sdist
                    if alt < dist[nei]:
                        dist[nei] = alt
                        pred[nei] = node
                        if nei == t:
                            raise Found
    except Found:
        pass

    # if pred[t] is None:
    #     pred[t] = s
    #     dist[t] = a[s][t]

    if dist[t] < a[s][t]:
        raise BadAns

    # print("Test", s, t)
    # print("Pred", pred)
    # print("Dist", dist)
    # print(a[s][t])
    global ans
    if dist[t] > a[s][t] and pred[t] is not None:
        print("Road", s, t)
        ans += a[s][t]

    # print("Pred", pred)
    # print("Dist", dist)

try:
    for i in range(n):
        for j in range(i + 1, n):
            # print("Check", i, j)
            dijk(i, j)
    print(ans)
except BadAns:
    print(-1)
