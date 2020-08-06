# counter함수를 쓴다.
# 최대값 = vales의 키값 중 리스트를 뽑는다.
# collections counter
# keys와 values를 리스트로 만들어 인덱스한다.

import sys
from collections import Counter
sys.stdin = open('input_data/4834.txt')

T = int(input())


for tt in range(1,T+1):
    t = int(input())
    numbers = input()
    my_numbers = 0
    lists = []
    for i in numbers:
        lists.append(int(i))
    count_lists = [0]*10
    for i in lists :
        count_lists[i] += 1
    max_value = count_lists[0]
    for i in range(len(count_lists)):
        if max_value <= count_lists[i]:
            max_value = count_lists[i]
            my_numbers = i
    print('#{} {} {}'.format(tt,my_numbers,max_value))
