import sys
sys.stdin = open("input.txt","r")
def inorder(v):
    global words
    if v == 0:
        return
    inorder(L[v])
    words += P[v]
    inorder(R[v])


for _ in range(1, 11):
    V = int(input())
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    for i in range(1, V + 1):
        data = list(input().split())
        P[i] = data[1]
        l = len(data)

        if l > 2:
            L[i] = int(data[2])
        if l > 3:
            R[i] = int(data[3])

    words = ''
    inorder(1)
    print('#{}'.format(_), words)


# def inorder(v):
#     global words
#     if v == 0:
#         return
#     inorder(L[v])
#     words += V[v]
#     inorder(R[v])
#
#
# for t in range(1, 11):
#     n = int(input())
#     V = [0] * (n + 1)
#     L = [0] * (n + 1)
#     R = [0] * (n + 1)
#     for i in range(1, n + 1):
#         info = list(input().split())
#         V[i] = info[1]
#         l = len(info)
#         if l > 2:
#             L[i] = int(info[2])
#         if l > 3:
#             R[i] = int(info[3])
#
#     words = ''
#     inorder(1)
#     print('#{}'.format(t), words)