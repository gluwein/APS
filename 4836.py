# 테스트 갯수는 3개이다.
# 행렬을 생성한다. -> 2차 LIST를 만든다. 2차리스트는 for문 두개로 만든다.
#   for i in range(len(arr))
#       for j in range(len(arr[0]))
# 해결책 1 x.y값을 불러온다? 그것이 서로 맞는지 비교해본다. 2차 LIST[x][y]값이 맞으면 카운트를 센다.
# 행넘버 갯수만큼 리스트를 생성한다.
# matrix = []
# for _ in hang_num:
#     matrix.append(_)
# hang_num = input()
# hang = input().split()
# for i in range(matrix)):
#     for j in range(matrix[0]):
# T = input()
# n,m = map(int, input(),split())
#
# mylist = [0]*n
#
# for i in range(n)
#     mylist[i] = list(map(int, input().split()))
#
# n,m = map(int,input().split())
# mylist = []
# for i in range(n):
#     mylist.append(list(map(int,input().split())))
# print(mylist)


'''
------x,y뽑는법---------
T = input()
s = int(input())
mylist = [0]*s
for i in range(s):
    mylist[i] = list(map(int, input().split()))
red = []
blue= []
for _ in range(s):
    for i in range(mylist[0][0],mylist[0][2]+1):
        for j in range(mylist[0][0],mylist[0][2]+1):
            red.append([i,j])
    print(red)
'''

import sys
sys.stdin = open('input_data/4836.txt')

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    red_lst = []
    blue_lst = []
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1,x2+1):
                if color == 1:
                    red_lst.append((y,x))
                if color == 2:
                    blue_lst.append((y,x))
    result = []
    for r in red_lst:
            if r in blue_lst:
                result.append(r)
    print('#{} {}'.format(tc,len(result)))

