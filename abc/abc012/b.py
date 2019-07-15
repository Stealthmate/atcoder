s = int(input())
h = s // 3600
m = (s % 3600) // 60
ss = s % 60
print("{:02}:{:02}:{:02}".format(h, m, ss))
