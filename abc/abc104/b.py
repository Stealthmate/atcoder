import re
p = re.compile("^A[a-z][a-z]*C[a-z]+$")
s = input()
print("AC" if p.match(s) is not None else "WA")
