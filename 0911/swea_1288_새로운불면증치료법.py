# 1288 새로운 불면증 치료법
# 조건
# N이 주어진다.
# 2N, 3N으로 값을 산출한다. -> int와 for 순회 (int는 알아서 순회가 된다)
# 공통되는 부분은 set을 사용한다.
# 4556 -> 4,5,5,7하는 방법은 무엇? range(len)을 사용하여 순회해서 하나씩 뽑아낸다.
# list에 각각 넣는다.
n = int(input())
for i in range(1, n+1):
    m = int(input())
    list = []
    for j in range(10000):
        list.append(j*m)
        while len(set(list)) == 10:
            break
