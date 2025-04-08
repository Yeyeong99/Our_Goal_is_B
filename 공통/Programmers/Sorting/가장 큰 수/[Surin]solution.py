"""
가장 큰수
0 or 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰수는?

방법
- 정렬 기준 >> A+B vs B+A 중 큰값이 되는 쪽이 앞으로
- 정렬된 결과 붙이기
- 맨 앞이 0이면 전체는 0
"""
from functools import cmp_to_key

def compare(a, b):
    if int(a + b) > int(b + a):
        return -1    # a가 앞
    elif int(a + b) < int(b + a):
        return 1    # b가 앞
    else:
        return 0    # 순서 유지한다.


def solution(numbers):
    numbers = list(map(str, numbers))    # 일단 문자열로 바꾸기

    answer = ''.join(sorted(numbers, key=cmp_to_key(compare)))
    
    if answer[0] == '0':
        return '0'
    
    return answer
