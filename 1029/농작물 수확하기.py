import sys
sys.stdin = open("농작물 수확하기.txt")


import math
a = math.floor(10/2)
TC = int(input())
N = int(input())
result = 0
for tc in range(1,TC+1):
    cnt = 0
    while cnt < N//2+1:
        i = str(input())
        standard = math.floor(N/2)
        sumlist = i[standard - cnt:standard + 1 + cnt]
        for i in sumlist:
            result += int(i)
        cnt += 1

    while cnt < N:
        j = str(input())
        standard2 = math.floor(N / 2)
        sumlist2 = j[((cnt)-N//2):N - cnt+N//2]
        for i in sumlist2:
            result += int(i)
        cnt += 1
    print("#{} {}".format(tc, result))
