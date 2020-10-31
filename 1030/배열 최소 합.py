def perm(k):
    if k == N:
        result = 0
        for r, c in enumerate(cols):
            
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k+1)
            cols[k], cols[i] = cols[i], cols[k]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    answer = 10000000 # 최종결과
    result = 0 # 부분합
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    while cnt < N:
        for i in range(N):
            result+=arr[i]
            for j in range(N):
                if i == j:
                    continue
                result += arr[j]












    if answer > result :
        answer = result


    print("#{} {}".format(tc, answer))

