arr = 'ABC'
N = 3

perm = []
def backtrack(k):
    if k == N:
        print(perm)

    else:

        for i in range(N): # 첫번째 요소
            if arr[i] in perm: continue
            perm.append(arr[i])
            backtrack(k+1)
            perm.pop()
backtrack(0)