T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    lists=[]
    counts = 0
    for _ in range(n):
        lists.append(list(map(int,input().split())))

    for i in range(n):
        sum_row = 0
        sum_column = 0
        for j in range(n):
            if lists[i][j] == 1:
                sum_row += 1
            else :
                if sum_row == m:
                    counts += 1
                sum_row = 0

            if lists[j][i] == 1:
                sum_column += 1
            else :
                if sum_column == m:
                    counts += 1 
                sum_column = 0

        if sum_row == m:
            counts += 1

        if sum_column == m:
            counts += 1

    print('#{} {}'.format(t+1,counts))