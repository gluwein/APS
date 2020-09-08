def bfs(queue):
    count = 1
    # 큐가 빌때까지 반복
    while queue:
        s_queue = []
        while queue:
            index = queue.pop()
            for i in node[index]:
                # 이미 방문했다면 넘어간다.
                if visited[i]: continue
                # 도착지와 일치한다면 이동거리를 반환한다.
                if i == end: return count
                # 위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
                s_queue.append(i)
                # 방문처리를 한다.
                visited[i] = 1
        count += 1
        queue = s_queue
    return 0


for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    start, end = map(int, input().split())
    visited[start] = 1
    print('#{} {}'.format(t, bfs([start])))