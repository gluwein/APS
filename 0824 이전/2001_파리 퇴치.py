import sys

sys.stdin = open('input_2001.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = tuple(map(int, input().split())) # 튜플형식으로 값을 나눕니다. N은 총 행렬의 크기이고 M은 파리채의 크기입니다. 
    result = [] # 빈 리스트를 하나 생성합니다. 왜냐하면
    catch = 0 # 잡은 파리의 수를 체크합니다.
    total = [] # catch를 더해서 최대값을 구할 때 씁니다. 
    for i in range(N):
        result += (list(map(int, input().split())))# 행렬을 만든다.
    for k in range(N - M + 1): # k의 의미는 파리채의 하나의 행의 순회를 말한다.
        for j in range(N - M + 1): # j의 의미는 파리채의 열의 순회를 말한다.
            for i in range(M): 
                catch += sum(result[k + i][j:j + M])
            total.append(catch)
            catch = 0
        
    print("#{} {}".format(t, max(total)))
