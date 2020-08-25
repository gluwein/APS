m = int(input())

for i in range(1, m+1):
    str1 = input()
    str2 = input()
    cnt, max_cnt = 0, 0

    for j in str1:
        for k in str2:
            if j == k:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0

    print('#{} {}'.format(i, max_cnt))