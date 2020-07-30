# 입력할 식을 만든다. 
# max() or 가장작은수를 변수로 정한 후 조건식
#조건식 가장작은수 > 변수 = 가장작은수 / 가장작은수 < 변수 = 변수
T = int(input())

for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    max_numbers = max(numbers)
    print('#{} {}'.format(t,max_numbers))