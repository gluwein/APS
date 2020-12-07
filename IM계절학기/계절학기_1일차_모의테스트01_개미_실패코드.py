import sys ; sys.stdin = open("10158_개미.txt")

m,n = map(int(input().split()))
x,y = map(int(input().split()))
num = int(input())

dx = {1,1,-1,-1} # 우하향, 우상향, 좌하향, 좌상향
dy = {1,-1,1,-1}

# 나누기? num % 2*m num % 2*n

while cnt < num :
    if x == m :
        x= x+dx[3]


