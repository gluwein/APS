import sys; sys.stdin = open("경비원.txt")

W,H = map(int, input().split())
TC = int(input())
store = []

def knowing_distance(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return W +H +(W-dist)
    elif dir == 3:
        return W + H + + W+ H -dist
    else:
        return W + dist


for tc in range(TC+1):
    if tc == TC :
        direction, distance = map(int, input().split())
    else :
        store.append(list(map(int, input().split())))

result = 0
dist1 = knowing_distance(direction,distance)
for i in range(TC) :
    dist2 = knowing_distance(store[i][0], store[i][1])
    path1 = abs(dist1-dist2)
    path2 = 2 * W + 2* H -path1
    if path1 < path2 :
        result += path1
    else :
        result += path2

print(result)