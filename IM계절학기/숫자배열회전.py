import sys ; sys.stdin = open("숫자배열회전.txt")

TC = int(input())
for tc in range(1, 1+TC):
    n = int(input())
    arr = [input().split() for _ in range(n)]

    list_90 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(arr[n-i-1][j])
        list_90.append(tmp)
    # print(list_90)

    list_180 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(list_90[n-i-1][j])
        list_180.append(tmp)
    # print(list_180)

    list_270 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(list_180[n-i-1][j])
        list_270.append(tmp)
    print(list_270)

    print('#{}'.format(tc))
    for i in range(n):
        print(''.join(list(map(str, list_90[i]))),''.join(list(map(str, list_180[i]))),''.join(list(map(str, list_270[i]))))




