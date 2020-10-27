import sys
sys.stdin = open("1961.txt.txt")

TC = int(input())
for tc in range(1,TC+1):
    n = int(input())
    arr = [list(map(str, input().split())) for _ in range(n)]
    # 90도로 회전한다.
    arr2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr2[i][j]=arr[n-j-1][i]
    result90 = [0]*n
    for i in range(n):
        result90[i] = ''.join(arr2[i])

    # 180도로 회전한다.
    for i in range(n):
        for j in range(n):
            arr2[i][j]=arr[n-1-i][n-1-j]
    result180 = [0]*n
    for i in range(n):
        result180[i] = ''.join(arr2[i])
    # 270도로 회전한다.
    for i in range(n):
        for j in range(n):
            arr2[i][j]=arr[j][n-1-i]
    result270 = [0]*n
    for i in range(n):
        result270[i] = ''.join(arr2[i])

    lastresult = [[0]*3 for i in range(n)]
    for i in range(3):
        for j in range(n):
            if i == 0:
                lastresult[j][i]= result90[j]
            elif i == 1:
                lastresult[j][i] = result180[j]
            elif i == 2:
                lastresult[j][i] = result270[j]
    print("#{}".format(tc))
    for lst in lastresult:
        print(' '.join(map(str, lst)))