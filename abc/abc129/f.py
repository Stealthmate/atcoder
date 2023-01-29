from math import ceil

L, A, B, M = map(int, input().split(" "))

digs = []
i = 0
while i < L:
    digs.append(i)
    d = len(str(A)) + len(digs) - 1
    current = A + i * B
    nexti = i + ceil((10 ** d - current) / B)
    i = nexti

ra = A % M
rb = B % M
ka = 1
for i in range(1, len(digs)):
    dec = 10 ** (len(str(A)) + i)
    dec = dec % M
    ka *= int(dec ** digs[i]) % M


print(digs)
