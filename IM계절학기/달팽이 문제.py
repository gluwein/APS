import sys ; sys.stdin = open("달팽이 문제.txt")
TC = int(input())
dx = [1,0,-1,0] # 우 하 좌 상
dy = [0,1,0,-1]

for tc in range(1,TC+1):
    tx = 0
    ty = 0
    num = 1
    f = 0
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    while (N*N) >= num:
        arr[ty][tx] = num
        num += 1
        nx = tx + dx[f]
        ny = ty + dy[f]
        if 0<=nx<N and 0<=ny<N and arr[ny][nx] ==0:
            tx = nx
            ty = ny

        else :
            f = (f+1)%4
            tx = tx + dx[f]
            ty = ty + dy[f]
    print("#{}".format(tc))
    for result in arr:
        print(*result)


