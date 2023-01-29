s = input()

last = len(s)
ans = 1
for i in reversed(range(len(s))):
    if s[i] == '?':
        print("? at", i)
        x = s[i+1:last]
        c = 0
        for j in range(10):
            y = int(str(j) + x)
            print("Test", y)
            if y % 13 == 0:
                print("y", y)
                c += 1
        # print("for ", x, c)
        ans = ans * c
        last = i
print(ans)
