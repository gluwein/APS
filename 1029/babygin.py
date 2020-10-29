import sys
sys.stdin = open("babygin.txt")
TC = int(input())
for tc in range(1, TC+1):
    carddummy = list(map(int, input().split()))
    player1 = []
    player2 = []
    cnt1 = 0
    cnt2 =0
    result1 = 0
    result2 = 0
    for i in range(0,len(carddummy),2):
        player1 += [carddummy[i]]
        cnt1 +=1
        if result1 == 1:
            break
        while cnt1 >3:
            if cnt1 == 7:
                result1 = 0
                break
            if player1[cnt1 - 2] == player1[cnt1-1] and player1[cnt1-1] == player1[cnt1]:
                result1 = 1
                break
            elif player1[cnt1 - 2]+1 == player1[cnt1 - 1] and player1[cnt1 - 1]+1 == player1[cnt1]:
                result1 = 1
                break
            elif player1[cnt1 - 2] == player1[cnt1 - 1] +1 and player1[cnt1 - 1] == player1[cnt1]+1:
                result1 = 1
                break
            else:
                break



    for j in range(1,len(carddummy)+1,2):
        player2 += [carddummy[j]]
        cnt2 +=1
        if result2 == 1:
            break
        while cnt1 >3:
            if cnt1 == 7:
                result2 = 0
                break
            if player1[cnt1 - 2] == player1[cnt1-1] and player1[cnt1-1] == player1[cnt1]:
                result2 = 1
                break
            elif player1[cnt1 - 2]+1 == player1[cnt1 - 1] and player1[cnt1 - 1]+1 == player1[cnt1]:
                result2 = 1
                break
            elif player1[cnt1 - 2] == player1[cnt1 - 1] +1 and player1[cnt1 - 1] == player1[cnt1]+1:
                result2 = 1
                break
            else:
                break
    if result1 == 0 and result2 == 0:
        print(0)
    if result1 == 1 and result2 == 0:
        print(1)
    if result1 == 1 and result2 == 1:
        if cnt1 >= cnt2 :
            print(1)
        else :
            print(2)


    # print(player1)
    # print(player2)

