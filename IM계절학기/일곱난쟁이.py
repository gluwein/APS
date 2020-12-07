import sys; sys.stdin = open("일곱난쟁이.txt")

arr = []
sum = 0
for i in range(9):
    arr.append(int(input()))
    sum += arr[-1]
arr.sort()
sum -= 100
k = 0
l = 0
for i in range(8):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == sum and i!=j:
            k,l = i,j
            # print(k,l)
            break
arr.pop(k)
arr.pop(l-1)
for answer in arr:
    print(answer)
