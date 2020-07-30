# 유효하다. 
# 유효하지 않다. 
# '#{} {}/{}/{}'.format(t,numbers[4],numbers[4:6],numbers[6:8])
T = int(input())



for t in range(1,T+1):
    numbers = (input())
    bad = '#{} -1'.format(t)
    good = '#{} {}/{}/{}'.format(t,numbers[:4],numbers[4:6],numbers[6:8])
    if int(numbers[4:6]) < 1 or int(numbers[4:6])> 12:
        print(bad)
    elif (int(numbers[4:6]) == 4 or 6 or 9 or 11) and int(numbers[6:8]) >30 :
        print(bad)
    elif int(numbers[4:6]) == 2 and int(numbers[6:8]) >28:
        print(bad)
    else:
        print(good)


    