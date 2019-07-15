s = input()
a = 0 < int(s[:2]) < 13
b = 0 < int(s[2:]) < 13
if a and b:
    print("AMBIGUOUS")
elif a:
    print("MMYY")
elif b:
    print("YYMM")
else:
    print("NA")
