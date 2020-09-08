import sys
sys.stdin = open("input.txt")

TC = int(input())


for i in range(1,TC+1):
    m = input()
    n = list(map(int, (input().split())))
    result=sorted(n)
    print('#{}'.format(i),end = " ")
    for j in result:
        print(j,end = " ")
    print()






