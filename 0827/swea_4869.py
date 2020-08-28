def _(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return _(x+10) + _(x+20) * 2


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print('#%d %s'%(tc, GetSome(0)))