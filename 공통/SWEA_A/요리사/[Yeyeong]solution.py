import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [_ for _ in range(N)]

    min_diff = float('inf')

    combs = list(combinations(ingredients, N // 2))
    len_combs = len(combs)
    for i in range(len_combs // 2):
        first = combs[i]
        second = combs[len_combs - i - 1]

        first_comb = list(combinations(first, 2))
        second_comb = list(combinations(second, 2))

        first_flavor = sum([synergies[i][j] + synergies[j][i] for i, j in first_comb])
        second_flavor = sum([synergies[i][j] + synergies[j][i] for i, j in second_comb])
        min_diff = min(abs(first_flavor - second_flavor), min_diff)
    print(f"#{t} {min_diff}")


