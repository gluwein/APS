TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    result = []

    #가로줄 확인
    galo_lst = []
    for i in range(N):
        Data = input()
        galo_lst.append(Data)
        for j in range(len(Data)-M+1):
            if Data[j:M+i] == Data[j:M+i][::-1]:
                result.append(Data[i:M+i])


    #세로줄 확인
