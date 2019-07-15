o = input()
e = input()
s = ""
for i in range(len(e)):
    s += o[i] + e[i]
s += o[len(o) - 1] if len(o) > len(e) else ""
print(s)
