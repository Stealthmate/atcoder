from collections import Counter
n = int(input())
ws = [input() for i in range(n)]
if len(Counter(ws)) < len(ws):
    print("No")
    exit(0)

for i in range(1, len(ws)):
    if ws[i][0] != ws[i-1][-1]:
        print("No")
        exit(0)
print("Yes")
