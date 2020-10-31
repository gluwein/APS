import sys
sys.stdin = open("농작물 수확하기.txt")


import math
TC = int(input())
N = int(input())
result = 0
for tc in range(1,TC+1):
    cnt = 0
    arr = [str(input()) for i in range(N)]
    for i in range(N):
        if i <= N//2:
            for i in range(N//2-1,)
            standard = math.floor(N/2)
            sumlist = arr[standard - cnt:standard + 1 + cnt]
            for arr in sumlist:
                result += int(arr)
            cnt += 1

        elif i == N//2+1:


        else :

    while cnt < N:
        j = str(input())
        standard2 = math.floor(N / 2)
        sumlist2 = j[((cnt)-N//2):N - cnt+N//2]
        for arr in sumlist2:
            result += int(arr)
        cnt += 1
    print("#{} {}".format(tc, result))
