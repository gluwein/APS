T= int(input())
for i in range(1,T+1):
    p, q, r, s, w = list(map(int, input().split()))
    a_price = 0
    b_price = 0
    result = 0
    a_price = w*p
    if r>w:
        b_price = q
    else:
        b_price = q + (w-r)*s
    if a_price > b_price:
        result = b_price
    else:
        result = a_price
    print('#{} {}'.format(i,result))