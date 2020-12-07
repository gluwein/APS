import sys ; sys.stdin = open("당근 수확2.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    carrot_arr = list(map(int, input().split()))
    cnt = 0
    N_namugi = 0
    for i in range(1,N+1):
        while carrot_arr[i-1] != 0:
            n = carrot_arr[i-1] // M
            cnt += n*2*i
            carrot_arr[i-1] -= n*M
            namugi = carrot_arr[i-1] % M
            N_namugi += namugi

            while N_namugi >= M:
                cnt += 2*i
                N_namugi -= M
            carrot_arr[i - 1] -= namugi

    if N_namugi > 0:
        cnt += 2*N


    print('#{} {}'.format(tc, cnt))