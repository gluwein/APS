import sys; sys.stdin = open("주사위.txt")

N = int(input())
arr = [ list(map(int,input().split())) for i in range(N)]
indicator = {0: 5, 1:3, 2:4, 3:1, 4:2, 5:0}
max_num = 0

for i in range(6):
    result = []
    tmp = [1,2,3,4,5,6]
    tmp.remove(arr[0][i])
    back = arr[0][i]
    tmp.remove(back)
    result.append(max(tmp))
    



