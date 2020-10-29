import sys
sys.stdin = open("컨테이너 운반.txt")

TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    Nlist = list(map(int, input().split()))
    Mlist = list(map(int, input().split()))
    Nlist.sort(reverse=True)
    Mlist.sort(reverse=True)
    res = []
    for burden in Nlist:
        for truck in Mlist:
            if burden <= truck:
                res.append(burden)
                Mlist.pop(0)
                break
    result = sum(res)
    print("#{} {}".format(tc+1, result))








