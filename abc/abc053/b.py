s = input()

start = s.index('A')
end = s[::-1].index('Z')
print(len(s) - end - start)
