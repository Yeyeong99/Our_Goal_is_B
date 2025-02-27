from collections import deque

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 숫자 개수, 번째
    N, K = map(int, input().split())

    # 16진수들
    numbers = list(input())

    # 회전해서 얻을 수 있는 숫자들
    total_numbers = []
    rotation_num = N//4
    for _ in range(rotation_num):
        for k in range(4):
            hex_num = ''.join(numbers[k*rotation_num:(k+1)*rotation_num])
            total_numbers.append(hex_num)

        numbers = deque(numbers)
        first = numbers.popleft()
        numbers.append(first)
        numbers = list(numbers)

    # 중복 제거
    total_numbers = [int(hex_n, 16) for hex_n in list(set(total_numbers))]

    # 내림차순
    for i in range(len(total_numbers)-1):
        for j in range(i, len(total_numbers)):
            if total_numbers[i] < total_numbers[j]:
                total_numbers[i], total_numbers[j] = total_numbers[j], total_numbers[i]

    answer = total_numbers[K-1]

    print(f'#{tc} {answer}')