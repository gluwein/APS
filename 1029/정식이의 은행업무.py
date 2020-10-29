import sys
sys.stdin = open("정식이의 은행업무.txt")

T = int(input())
for t in range(T):
    b = input()
    c = input()
    lb, lc = len(b), len(c)
    bb, cc = 0, 0
    ab, ac = [], []

    for k in range(lb):
        if int(b[k]):
            bb += 2 ** (lb - k - 1)
    for k in range(lc):
        if int(c[k]):
            cc += 3 ** (lc - k - 1) * int(c[k])

    for i in range(1, lb):
        if int(b[i]):
            ab.append(2 ** (lb - 1 - i) * (-1) + bb)
        else:
            ab.append(2 ** (lb - 1 - i) + bb)
    for i in range(lc):
        if int(c[i]) == 2 and i == 0:
            pn = [-1]
        elif int(c[i]) == 1 and i == 0:
            pn = [1]
        elif int(c[i]) == 2:
            pn = [-1, -2]
        elif int(c[i]) == 1:
            pn = [-1, 1]
        else:
            pn = [1, 2]
        for k in pn:
            ac.append(3 ** (lc - 1 - i) * k + cc)
    for p in ab:
        if p in ac:
            print('#{} {}'.format(t + 1, p))
            break