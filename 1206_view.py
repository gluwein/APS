# 리스트로 전 후롤 탐색한다.
# 최대값을 구한다. 
# 해당 값과 최대값을 뺀다.
import sys
sys.stdin = open('input_data/1206.txt')

for tc in range(1,11):
    result = 0
    n = int(input())
    my_list = list(map(int,input().split()))
    for t in range(2,n-2):
        twotwo = max(my_list[t-2],my_list[t-1],my_list[t+1],my_list[t+2])
        if my_list[t]>twotwo :
            result += my_list[t] - twotwo

    print('#{} {}'.format(tc,result))

