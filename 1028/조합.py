arr = ['A','B','C'] ; N = len(arr)

for i in range(N-1):
    for j in range(i + 1, N):
        print(arr[i], arr[j])
print('-------------')
# 5C3
arr2 = ['A','B','C','D','E'] ; N = len(arr2)
for i in range(N-2):
    for j in range(i + 1, N -1):
        for k in range(j+1, N):
            print(arr2[i], arr2[j], arr2[k])