n, t = map(int, input().split(" "))

lastOpened = 0
total = 0
for i in range(n):
    tt = int(input())

    if lastOpened == 0:
        lastOpened = tt
    elif lastOpened + t >= tt:
        total += tt - lastOpened
        # print("Reopen", tt, total)
        lastOpened = tt
    else:
        total += t
        lastOpened = tt
total += t
print(total)
