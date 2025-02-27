
from collections import deque

def rotate(n, number_list):                     # 숫자 개수랑 숫자들 입력받음
    for i in range(n-1):                        # n-1 만큼 돔
        stack = []
        for numnum in number_list:                              # len(number_list) / 4만큼 number_list를 짝지어줌
            stack.append(numnum)
            if len(stack) == (len(number_list) / 4):
                if stack not in num_16:
                    num_16.append(stack)
                stack = []
        number_list.rotate(1)                   # number_list를 시계방향으로 회전

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, K = map(int, input().split())                     # N은 숫자의 개수 / 크기 숫자 K
    numbers = deque(input())                             # N개의 숫자

    num_16 = []                                          # 16진수 숫자들
    num_10 = []                                          # 10진수 숫자들

    rotate(N, numbers)                                   # 숫자의 개수랑 numbers 받음

    num_16.sort(reverse=True)                            # 내림차순 나열


    for num in num_16:                                   # 16진수 숫자들 10진수로 변환
        link = ''.join(num)
        num_10.append(int(link, 16))                      # 16진수 -> 10진수 변환한 숫자 리스트에 추가

    result = num_10[K-1]                                 # K번째 숫자

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
