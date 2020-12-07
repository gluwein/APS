

dx = [0,1,0,-1]
dy = [1, 0, -1, 0]

R, C = map(int, input().split())

K = int(input())

if K > C*R:
    print(0)
else:
    arr = [[0]*C for _ in range(R)]

    d = 0
    r = 0
    c = 0
    num = 1

    while True:
        arr[r][c] = num
        if num == K:
            break
        num += 1

        tx = r + dx[d]
        ty = c + dy[d]
        if 0<= tx < R and 0 <= ty <C and arr[tx][ty] ==0:
            r, c = tx, ty
        else:
            d = (d+1)%4
            r += dx[d]
            c += dy[d]
    print(r+1, c+1)
