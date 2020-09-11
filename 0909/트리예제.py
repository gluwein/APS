import sys
sys.stdin = open("tree_input.txt", "r")
V,E = map(int,input().split()) # 정점수, 간선수
arr = list(map(int, input().split()))

L = [0]*(V+1) # V+1을 하는이유는 루트의 인덱스값이 0이 아닌 1이기 때문이다.
R = [0]*(V+1)
P = [0]*(V+1)

for i in range(0, E*2,2): # E는 간선수이다.
    p,c = arr[i], arr[i+1] # 부모노드, 자식노드
    P[c] = p
