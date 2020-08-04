# 첫 째 입력값은 .format 으로 넣는다.
# 맨오른 쪽은 최대값으로 맨왼쪽은 최소값으로 만든다.
# 차를 구한다.
# for문을 쓴다.
# a1 < a2 : 
# a[1], a[2] = a[2] , a[1]
# a[i]
import sys 
sys.stdin = open('input_data/4828.txt')


T = int(input())

for tt in range(T):
    t = int(input())
    lists = list(map(int,input().split()))
    for i in range(t-1):
        if lists[i] < lists[i+1]:
            lists[i],lists[i+1] = lists[i+1], lists[i]
    my_min = lists[-1]
    for i in range(t-1):
        if lists[t-1-i] > lists[t-1-(i+1)]:
            lists[(t-1)-i],lists[(t-1)-(i+1)] = lists[(t-1)-(i+1)], lists[(t-1)-i]
    my_max = lists[0]
    print('#{} {}'.format(tt+1, my_max - my_min))
