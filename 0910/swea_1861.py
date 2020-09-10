
for tc in range(1, int(input()) + 1):
    N,M = map(int, input().split()) # 사람수
    G = [[] for _ in range(N+1)]






    visit = [0]*(N+1)

    def dfs(V):
        pass

    for i in range(1, N+1):
        if not visit[i]:
            dfs(i)