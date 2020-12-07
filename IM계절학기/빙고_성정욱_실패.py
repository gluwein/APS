import sys; sys.stdin = open("빙고.txt")

arr = []
for _ in range(5):
    arr.append(list(map(int,input().split())))
cnt = 0
result = 0
speaker = []
garo_arr = []
d = 4
g = 0
e = 0
f = 0
for s in range(5):
    speaker.append(list(map(int,input().split())))
for i in range(5): #ij는 부르는 것
    for j in range(5):
        speaker_delete = speaker[i][j]
        for k in range(5): # kl은 빙고
            for l in range(5):
                if arr[k][l] == speaker_delete :
                    arr[k][l] = 0
                    cnt +=1
                    if cnt >= 12:
                        for m in range(5):
                            if arr[m] == [0, 0, 0, 0, 0]:
                                result += 1
                            for n in range(5):
                                garo_arr.append(arr[n][m])
                            if garo_arr == [0, 0, 0, 0, 0]:
                                result += 1
                            garo_arr = []
                        while d >= 0 and g <= 4:
                            if arr[d][g] == 0:
                                d -= 1
                                g += 1
                            else:
                                break
                        if d == -1 and g == 5:
                            result += 1
                        while e <= 4 and f <= 4:
                            if arr[e][f] == 0:
                                e += 1
                                f += 1
                            else:
                                break
                        if e == 5 and f == 5:
                            result += 1
                        if result == 3:
                            print(cnt)

