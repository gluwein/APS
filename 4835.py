import sys
sys.stdin = open('input_data/4835.txt')

T = int(input())
for tt in range(1,T+1):
    N,M = list(map(int,input().split()))
    my_number = list(map(int,input().split()))
    my_list = []
    for my_count in range(N-M+1):
        my_list.append(sum(my_number[my_count:my_count+M]))
    zero1 = 0
    zero2 = float('inf')
    for i in range(len(my_list)):
        if my_list[i]>=zero1:
            zero1 = my_list[i]
    for i in range(len(my_list)):
        if my_list[i]<=zero2:
            zero2 = my_list[i]
    result = zero1 - zero2
    print('#{} {}'.format(tt,result))




