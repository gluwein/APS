import sys ; sys.stdin = open("연속한 1의 개수.txt")

TC = int(input())
for tc in range(TC):
    cnt = 0
    max_cnt = 0
    num = int(input())
    str = input()

    for i in range(num):
        if str[i] == '1':
            cnt += 1
            if max_cnt <cnt :
                max_cnt = cnt
        if str[i] == '0':
            cnt = 0
    print('#{} {}'.format(tc+1, max_cnt))

