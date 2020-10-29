arr = [69, 10, 30, 2, 16, 8, 31, 22, 30]
N = len(arr)

#최소값 구하기
def getMin(s, e):
    # 기저사례 (함수호출 종료)
    if s == e :
        return s
    else:
        ret = getMin(s, e - 1)  # 더 작은 문제에 대해서 호출
        return ret if arr[ret] < arr[e] else e

print(getMin(0,N-1))
