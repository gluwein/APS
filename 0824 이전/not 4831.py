# 포함한다면, count 한다.
# 시작은 start = 0 count = 0

# cond = list(map(int,input().split()))
# lists = list(map(int,input().split()))

for t in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    station = [0[*(N+1)]]
    for val in numbers:
        station = [0]*(N+1)

    bus = 0
    ans = 0
    while bus + K < N :
        for i in range(bus + K, bus, -1):
            if station[i]:
                bus = i
                ans +=1
                break
        if bus == prev:
            ans = 0; break



start = 0
count = 0
#T = int(input())
cond = [3,10,5]
lists = [1,3,5,7,9]
while start != lists[-1] or start < lists[-1]:
    if start + cond[0] in lists :
        count += 1
        start += cond[0]
    elif start + cond[0]-1 in lists :
        count += 1
        start += cond[0]-1
    elif start + cond[0]-2 in lists :
        count += 1
        start += cond[0]-2
    elif start + cond[0]-3 in lists :
        count += 1
        start += cond[0]-3
if count > cond[2] :
    print(0)
else :
    print(count)