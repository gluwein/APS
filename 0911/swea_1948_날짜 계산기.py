

n = int(input())
lists=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1,n+1):
    a, b, c, d = list(map(int, input().split()))
    month_by_days = lists[a-1:c-1]
    large_number = 0
    small_numbers = 0
    for j in month_by_days:
        large_number +=j
    small_numbers = d-b+1
    result = large_number + small_numbers
    print('#{} {}'.format(i,result))
