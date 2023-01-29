n = int(input())
a = list(map(int, input().split(" ")))

print(' '.join([str(i+1) for i,x in sorted(enumerate(a), key=lambda x: x[1])]))
