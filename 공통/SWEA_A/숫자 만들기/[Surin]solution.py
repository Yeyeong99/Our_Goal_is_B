def dfs(i, current_result):
    global max_sum, min_sum

    # 1. 재귀 중단 파라미터 설정 : 숫자카드의 마지막 수까지 계산했다면
    if i == N - 1:
        # 큰 값을 찾아줘
        max_sum = max(max_sum, current_result)
        min_sum = min(min_sum, current_result)
        return

    # 2. 계속 가져가고 싶은 것은? : 계산 결과
    for j in range(4):
        if operators[j] > 0:  # 해당 연산자가 남아있다면
            operators[j] -= 1  # 사용함.
            current_card = number_list[i + 1]

            if j == 0:
                dfs(i + 1, current_result + current_card)
            elif j == 1:
                dfs(i + 1, current_result - current_card)
            elif j == 2:
                dfs(i + 1, current_result * current_card)
            elif j == 3:
                if current_result < 0:  # 음수이면
                    dfs(i + 1, -(-current_result // current_card))
                else:
                    dfs(i + 1, current_result // current_card)

            operators[j] += 1


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    # 숫자의 개수
    N = int(input())

    # 연산자 카드 + - * /
    symbol_counts = list(map(int, input().split()))

    # 숫자 카드
    number_list = list(map(int, input().split()))

    # 최대, 최소
    max_sum = float('-inf')
    min_sum = float('inf')

    operators = symbol_counts[:]

    dfs(0, number_list[0])

    answer = max_sum - min_sum

    print(f'#{tc} {int(answer)}')