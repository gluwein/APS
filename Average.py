T = int(input())
for t in range(1,T+1):
    numbers =list(map(int,input().split()))
    my_sum = 0
    my_count = 0
    for number in numbers:
        my_sum += number
        my_count += 1
        result = int(round((my_sum/my_count),0))
    print('#{} {}'.format(t,result))  
