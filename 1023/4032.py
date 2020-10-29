import sys; sys.stdin = open('4013.txt','r')
from collections import deque


for tc in range(1, int(input() +1)):
    K = int(input()) # 회전 작업수
    Q = [[]] + [list(map(int, input().split())) for _ in range(4)] #자석정보


    check = [0]*5

    