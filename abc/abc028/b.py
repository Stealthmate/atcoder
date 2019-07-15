from collections import Counter

s = input()
d = { k: 0 for k in "ABCDEF" }
d.update(Counter(s).most_common())
print(' '.join([ str(v) for k, v in sorted(d.items(), key=lambda x: x[0])]))
