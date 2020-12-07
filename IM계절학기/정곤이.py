import sys; sys.stdin = open("정곤이.txt")

def danjo_check(number):
    number_length = str(number)
    for k in range(len(number_length)-1):
        if number_length[k] < number_length[k+1]:
            return True
        else:
            return False

TC = int(input())
for tc in range(1, TC+1 ):
    N= input()
    arr = list(map(int, input().split()))
    result = -1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            num = arr[i]*arr[j]

            if result < num and danjo_check(num) :
                result = num
    print("#{} {}".format(tc, result))



