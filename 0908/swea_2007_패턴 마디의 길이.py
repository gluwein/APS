import sys

sys.stdin = open("input.txt", "r")
t = int(input())

for j in range(1,t+1):
    lists = input()

    for i in range(2,len(lists)):
        if lists[:i] == lists[i:(i)*2]:
            print("#{} {}".format(j, i))
            break
 