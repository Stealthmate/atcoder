from itertools import chain
n = int(input())

n1 = (n // 5) % 6
s = list(str("123456"))
s = s[n1:] + s[:n1]
n2 = n % 5
if n2 >= 1:
    s = list(chain(s[1:n2 + 1], [s[0]], s[n2 + 1:]))
print(''.join(s))
