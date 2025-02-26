import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")


def dfs(idx, result):
    global result_max
    global result_min

    if idx == N - 1:
        result_max = max(result_max, result)
        result_min = min(result_min, result)
        return

    for e in range(4):
        if operators[e] > 0:
            operators[e] -= 1
            if e == 0:
                new_result = result + numbers[idx + 1]
            elif e == 1:
                new_result = result - numbers[idx + 1]
            elif e == 2:
                new_result = result * numbers[idx + 1]
            elif e == 3:
                new_result = int(result / numbers[idx + 1])

            dfs(idx + 1, new_result)
            operators[e] += 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    result_max = -float('inf')
    result_min = float('inf')

    dfs(0, numbers[0])
    print(f"#{t} {result_max - result_min}")






