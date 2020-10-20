 def isSafe(i, j):
    return -1 < i < mazesize and -1 < j < mazesize and maze[i][j] != 1


T = int(input())
for test_case in range(1, T + 1):
    mazesize = int(input())

    maze = []
    for i in range(mazesize):
        maze.append(list(map(int, ''.join(input().split()))))

    for i in range(mazesize):
        for j in range(mazesize):
            if maze[i][j] == 2:
                xs, ys = [i, j]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = [[xs, ys]]
    visit = [[0]*mazesize for _ in range(mazesize)]
    visit[xs][ys] = 1
    dist = [[0]*mazesize for _ in range(mazesize)]
    result = 0
    while queue:
        curr = queue.pop(0)
        for dir in range(4):
            ddx = dx[dir]
            ddy = dy[dir]
            if isSafe(curr[0]+ddx, curr[1]+ddy) and visit[curr[0]+ddx][curr[1]+ddy] == 0:
                if maze[curr[0]+ddx][curr[1]+ddy] == 3:
                    result = dist[curr[0]][curr[1]]
                    break
                queue.append([curr[0]+ddx, curr[1]+ddy])
                visit[curr[0]+ddx][curr[1]+ddy] = 1
                dist[curr[0]+ddx][curr[1]+ddy] = dist[curr[0]][curr[1]] + 1

    print('#%d %d' % (test_case, result))