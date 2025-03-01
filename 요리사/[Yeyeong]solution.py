import sys
sys.stdin = open("input.txt", "r")


def dfs(i, selected_idx, current_sum, total_sum):
    global min_diff
    if i > N:
        return
    # 두 개의 인덱스가 선택 됨
    if len(selected_idx) == 2:
        x = selected_idx[0]
        y = selected_idx[1]
        current_sum += [synergies[x][y] + synergies[y][x]]
        selected_idx = []

    # 식재료 절반이 선택 됨
    if len(current_sum) == N // 2 and total_sum == 0:
        total_sum = sum(current_sum)
        current_sum = []

    # 식재료가 모두 선택됨: 두 번째 합을 빼줌
    elif len(current_sum) == N // 2 and total_sum != 0:
        total_sum -= sum(current_sum)
        min_diff = min(abs(total_sum), min_diff)
        return
    ingredient = ingredients[: i] + ingredients[i + 1:]
    for j in ingredient:
        dfs(j, selected_idx, current_sum, total_sum)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [_ for _ in range(N)]

    min_diff = float('inf')

    for n in ingredients:
        dfs(n, [], [], 0)

    print(t, min_diff)

