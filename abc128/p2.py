N = int(input())
Ss, Ps = [ [], [] ]
for i in range(N):
    s, p = input().split(" ")
    Ss.append(s)
    Ps.append(int(p))
rests = list(zip(range(1, N+1), Ss, Ps))
rests.sort(key=lambda x: (x[1], -x[2]))
print('\n'.join([str(i) for i,_,_ in rests]))
