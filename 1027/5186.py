import sys
sys.stdin = open("5186.txt")
TC = int(input())

for tc in range(1,TC+1):
    a=float(input())
    list = []
    for _ in range(0,13):
        if a*2**_ >=0.5 :
            list.append('1')
            a -= (0.5)**(_+1)
            if a == 0:
                break

        else :
            list.append('0')

    if a != 0:
        result = 'overflow'
    else :
        result = ''.join(list)

    print("#{} {}".format(tc, result))


