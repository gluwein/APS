T = int(input())
for i in range(1,T+1):
    m,n = list(map(int,input().split()))
    if m>n:
        for j in range(m-n):
            for i in range(len(m)):
                result.append(m[i+j]*n[i])