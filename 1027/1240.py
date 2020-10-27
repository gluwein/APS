import sys
sys.stdin=open("1240.txt")


codenumber = {'0001101':0,'0011001':1,'011101':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())

    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][M-1-j] == '1':





