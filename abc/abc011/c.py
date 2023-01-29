n, ng1, ng2, ng3 = [int(input()) for i in range(4)]

ngs = [ng1, ng2, ng3]

op = 100
ans = n
while op > 0 and ans > 0:
    t = ans
    if ans in ngs:
        break
    if ans - 3 not in ngs:
        t -= 3
    elif ans - 2 not in ngs:
        t -= 2
    elif ans - 1 not in ngs:
        t -= 1
    if t == ans:
        break
    ans = t
    op -= 1

print("YES" if ans <= 0 else "NO")
