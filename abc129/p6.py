from multiprocessing import Pool

def calc_rem(arg):
    A, B, x = arg
    return (A + B*x)

def main():

    L, A, B, M = map(int, input().split(" "))

    rems = []


    with Pool(processes=5) as p:
        rems = p.map(calc_rem, zip([A] * L, [B] * L, range(L)))

    rem = 0
    for i in range(L):
        si = rems[i]
        ndigs = len(str(si))
        remsi = si % M
        rem = ((rem * (10 ** ndigs)) + remsi) % M
    print(rem)

if __name__ == '__main__':
    main()
