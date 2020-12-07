import sys; sys.stdin =open(" 꽃가루.txt")

dx = [1,0,-1,0]
dy = [0,-1,0,1]

TC = int(input())
for tc in range(1, TC+1):
    N,M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N):
        for j in range(M):
            sum = 0

            sum += arr[i][j]
            for _ in range(arr[i][j]):
                tx = j + dx[0]*(_+1)
                ty = i + dy[0]*(_+1)
                if 0<=tx<M and 0<=ty<N:
                    sum += arr[ty][tx]
            for _ in range(arr[i][j]):
                tx = j + dx[1]*(_+1)
                ty = i + dy[1]*(_+1)
                if 0<=tx<M and 0<=ty<N:
                    sum += arr[ty][tx]
            for _ in range(arr[i][j]):
                tx = j + dx[2]*(_+1)
                ty = i + dy[2]*(_+1)
                if 0<=tx<M and 0<=ty<N:
                    sum += arr[ty][tx]
            for _ in range(arr[i][j]):
                tx = j + dx[3]*(_+1)
                ty = i + dy[3]*(_+1)
                if 0<=tx<M and 0<=ty<N:
                    sum += arr[ty][tx]
            if sum >= max_sum :
                max_sum = sum
    print("#{} {}".format(tc,max_sum))
