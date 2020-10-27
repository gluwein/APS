n,m = map(int, input().split())
if 0 < n < 101 and 0<m<4
    if m == 1:
        for i in range(1,n+1):
            print('*'*i)
    elif m == 2:
        for j in range(n,0,-1):
            print('*'*j)
    elif m == 3:
        for k in range(1,n+1):
            print("{}{}".format(' '*(n-k),'*'*(2*k-1)))
else :
    print("INPUT ERROR!")