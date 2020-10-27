import sys
sys.stdin = open("5185.txt")
TC = int(input())



for tc in range(TC):
    list = []
    number, six = input().split()
    for i in six:

        sixteen = int(i, 16)
        list.append('1' if sixteen & 8 else '0')
        list.append('1' if sixteen & 4 else '0')
        list.append('1' if sixteen & 2 else '0')
        list.append('1' if sixteen & 1 else '0')
    print("#{} {}".format(tc+1, ''.join(list)))

