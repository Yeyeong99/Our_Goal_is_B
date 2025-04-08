"""
가장 큰수
0 or 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰수는?

방법
- 정렬 기준 >> A+B vs B+A 중 큰값이 되는 쪽이 앞으로
- 정렬된 결과 붙이기
- 맨 앞이 0이면 전체는 0
"""

def solution(numbers):
    for a in range(0, len(numbers)-1):
        for b in range(a+1, len(numbers)):
            str_a, str_b = str(numbers[a]), str(numbers[b])
            if int(str_a + str_b) < int(str_b + str_a):
                numbers[a], numbers[b] = numbers[b], numbers[a]

    answer = ''.join(map(str, numbers))
    return answer


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
