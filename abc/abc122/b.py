import re
s = input()
ans = [re.search("[AGCT]*", s[i:]) for i in range(len(s))]
ans = max([len(x.group(0)) if x else 0 for x in ans])
print(ans)
