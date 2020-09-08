# zero ~ nin까지 수가 규ㅣㄱ없이 정렬되어있다.

# 기초 체계를 만든다.


# 변수를 List화 하고 count_0~10까지 정한다.

# if 와 count를 사용한다.

# 각 변수의 갯수를 알고 그것들을 반복한다.

# zro one two~ thr for fiv 순으로 젇렬을 한다.

import sys
sys.stdin = open("input.txt", "r")


n = int(input())
for i in range(1,n+1):
    k = input()
    m = list(input().split())
    result = []
    for j in m:
        if 'ZRO' == j:
            result.append('ZRO')
    for j in m:
        if 'ONE' == j:
            result.append('ONE')
    for j in m:
        if 'TWO' == j:
            result.append('TWO')
    for j in m:
        if 'THR' == j:
            result.append('THR')
    for j in m:
        if 'FOR' == j:
            result.append('FOR')
    for j in m:
        if 'FIV' == j:
            result.append('FIV')
    for j in m:
        if 'SIX' == j:
            result.append('SIX')
    for j in m:
        if 'SVN' == j:
            result.append('SVN')
    for j in m:
        if 'EGT' == j:
            result.append('EGT')
    for j in m:
        if 'NIN' == j:
            result.append('NIN')
    print('#{}'.format(i))
    for k in result :
        print(k, end=" ")

