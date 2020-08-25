m = int(input())

for i in range(1, m+1):
    str1 = input()
    str2 = input()

    result = 0
    for j in range(len(str2)-len(str1)+1):
        if str2[j:j+len(str1)] == str1:
            result = 1

    print('#%d %s'%(i, result))