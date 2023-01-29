from math import floor, ceil

deg, dis = map(int, input().split(" "))
deg /= 10
dis = dis / 6.0
if dis % 1 >= 0.5:
    dis = ceil(dis) / 10
else:
    dis = floor(dis) / 10
dr = floor((deg + 11.25) / 22.5)
drs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
if dr >= len(drs):
    dr = 0
dr = drs[dr]

ds = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, float("inf")]
i = 0
while dis > ds[i]:
    i += 1

if i == 0:
    dr = 'C'

print(dr, i)
