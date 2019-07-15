n = int(input())
s = 0
for i in range(n):
    a, b = input().split(" ")
    a = float(a)
    s += a * {"JPY": 1, "BTC": 380000}[b]
print(s)
