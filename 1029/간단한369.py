import sys
sys.stdin = open("간단한369.txt")

N = int(input())
i = 1

while i < N + 1 :
    cnt = 0
    j = i
    while j/10 > 1:
        if i % 10 == 3 or i % 10 == 6 or i%10 == 9 :
            cnt +=1
            j = j//10
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            cnt += 1
            j = j // 10
        else :
            break
    if cnt == 0:
        if i % 10 == 3 or i % 10 == 6 or i%10 == 9 :
            cnt +=1
            print(cnt * '-', end=" ")
        else:
            print(i,end=" ")
        i += 1
    else :
        print(cnt*'-', end=" ")
        i += 1
