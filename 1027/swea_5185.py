import sys
sys.stdin = open("5185.txt")

result = ''
def binary(num):
    global result
    mok = nam = 0
    for _ in range(4):
        nam = num % 2
        result = str(nam)+result
        num = num // 2
    return result


TC = int(input())
number, sixteen = input().split()
n = int(number)

change = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for i in range(sixteen):
    if isdigit(i):
        pass
    else :

