import sys ; sys.stdin = open("당근 수확.txt")


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    a = list(map(int,(input().split())))

    min_carrot_num = 10000000000000
    carrot_num = 0
    carrot_num1 = 0
    carrot_num2 = 0
    min_num = 0
    for num in range(N):
        for i in a[:num+1]:
            carrot_num1 += i
        for j in a[num+1:]:
            carrot_num2 += j
        carrot_num = abs(carrot_num1 - carrot_num2)
        if carrot_num < min_carrot_num :
            min_carrot_num = carrot_num
            min_num = num+1
        carrot_num1 = 0
        carrot_num2 = 0

    print('#{} {} {}'.format(tc, min_num, min_carrot_num))