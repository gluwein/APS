for test_case in range(1, 11):
    number = int(input())
    matirix = list()
    for_sum = list()

    # 가로
    for _ in range(100):
        line = list(map(int, input().split()))
        for_sum.append(sum(line))
        matirix.append(line)

    # 세로
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += matirix[j][i]
        for_sum.append(sum_num)

    # 오른쪽 대각선 
    sum_num = 0
    for i in range(100):
        sum_num += matirix[i][i]
    for_sum.append(sum_num)

    # 왼쪽 대각선
    sum_num = 0
    for i in range(100):
        sum_num += matirix[i][99-i]
    for_sum.append(sum_num)

    print("#{} {}".format(number, max(for_sum)))
