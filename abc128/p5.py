N, Q = [int(x) for x in input().split(" ")]
stops = []
people = []
for i in range(N):
    stops.append([int(x) for x in input().split(" ")])
stops.sort(key=lambda x: x[1])

for i in range(Q):
    # people.append(int(input))
    start = int(input())
    dist = 0
    for s in stops:
        block = s[1] - 1
        print("Time", start + block, "At stop", (s[0] - 0.5, block, s[2] - 0.5))
        if s[0] - 0.5 <= start + block <= s[2] - 0.5:
            dist = s[0]
            break
        dist = s[2]
    print(dist)
        
        
