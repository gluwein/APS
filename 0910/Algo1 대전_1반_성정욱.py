T = int(input())
dx = [0,0,-1,-1]
dy = [-1,1,0,0]

# 반복문을 이용해서 DFS사용
def dfs(i,j):
    global visited

    stack = []

    stack.append([i,j])
    top = 0

    while stack:

        pos = stack[top]

        if visited[pos[1]pos[0]] == 0:
            visited[pos[1]pos[0]] = 1

        else:

        for d in range(4):
            moving_x = pos[0]+dx[d]
            moving_y = pos[1]+dy[d]





for tc in range(T):
    #행과 열 M,N
    M,N = map(int, input().split())

    Trees = [[0 for _ in range(M)]*N]






