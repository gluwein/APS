def dfs(idx):
    global count
    count += 1
    for i in Tree[idx]:
        dfs(i)


for t in range(int(input())):
    V, N = map(int, input().split())
    temp_list = input().split()
    Tree = [[] for _ in range(V + 2)]
    for idx, i in enumerate(range(0, V * 2, 2)):
        a = int(temp_list[i])
        b = int(temp_list[i + 1])
        Tree[a].append(b)
    count = 0
    dfs(N)
    # 결과값 출력
    print('#{} {}'.format(t + 1, count))