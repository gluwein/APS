import sys
sys.stdin = open('input_data/1208.txt')

T = 10
for tt in range(1,T+1):
    dump = int(input())
    m= list(map(int, input().split()))
    mountain = []
    for i in m:
        mountain.append(i)
    zero1 = 0
    zero2 = float('inf')
    for i in range(dump):
        for l in range(len(mountain)):
            if zero1 <= mountain[l]:
                zero1 = mountain[l]
        print(zero1)
        for s in range(len(mountain)):
            if zero2 >= mountain[s]:
                zero2 = mountain[s]
        zero1 -= 1
        zero2 += 1
        result = zero1 - zero2
    print('#{} {}'.format(tt,result))
 



    # for my_count in range(N-M+1):
    #     my_list.append(sum(my_number[my_count:my_count+M]))
    # zero1 = 0
    # zero2 = float('inf')
    # for i in range(len(my_list)):
    #     if my_list[i]>=zero1:
    #         zero1 = my_list[i]
    # for i in range(len(my_list)):
    #     if my_list[i]<=zero2:
    #         zero2 = my_list[i]
    # result = zero1 - zero2
    # print('#{} {}'.format(tt,result))



