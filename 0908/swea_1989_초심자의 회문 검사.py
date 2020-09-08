import sys

sys.stdin = open("input.txt", "r")


m = int(input())
for i in range(1,m+1):
    n = input()
    if n == n[::-1]:
        print('#{}'.format(i),1)
    else:
        print('#{}'.format(i),0)