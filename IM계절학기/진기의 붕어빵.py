import sys ; sys.stdin = open("진기의 붕어빵.txt")


TC = int(input())
for tc in range(1,TC+1):
    N,M,K = map(int, input().split())
    consumer = list(map(int, input().split()))
    consumer.sort()
    # print(consumer)
    bbang = 0
    result = 'Possible'
    cnt = 0
    for i in range(N):
        arr = [0]*(N*M+1)

    for j in range(M,M*N+1,M):
        arr[j] = K
    # print(arr)
    for k in consumer:
        cnt += 1
        for l in arr[:k+1]:
             bbang += l
        if bbang < cnt:
            result = 'Impossible'
        bbang = 0

    print("#{} {}".format(tc,result))

