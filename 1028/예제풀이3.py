arr = 'ABC'
N = 3

# 순열을 만들기 위해
# 주어진 N 개의 요소에서 (순서대로) 하나씩 선택하는 작업

perm = []
for i in range(N): # 첫번째 요소
    # if arr[i] in perm: continue
    perm.append(arr[i])
    for j in range(N):  # 두번 째 요소
        # if arr[j] in perm: continue
        perm.append(arr[j])

        for k in range(N):  # 세번 째 요소
            # if arr[k] in perm: continue
            perm.append(arr[k])

            print(perm)
            perm.pop()
        perm.pop()
    perm.pop()