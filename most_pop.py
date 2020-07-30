#최빈값을 구한다. 
# 범위 -> List 순회
# 찾을 값은 순회하는 수 중의 하나를 고름

# for number in numbers:
#     my_count = numbers.count(number)
from collections import Counter 
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(Counter(colors))