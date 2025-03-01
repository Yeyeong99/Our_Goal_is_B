import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]
    ingredient = [_ for _ in range(N)]

    min_diff = float('inf')
    combs = sorted(list(set(combinations(ingredient, N // 2))))
    for i in range(len(combs)):
        x = combs[i][0]
        y = combs[i][1]
        first_dish = synergies[x][y] + synergies[y][x]
        for j in range(i + 1, len(combs)):
            if len(set(list(combs[i]) + list(combs[j]))) == N:
                z = combs[j][0]
                k = combs[j][1]

                second_dish = synergies[z][k] + synergies[k][z]

                diff = abs(first_dish - second_dish)
                min_diff = min(min_diff, diff)

    print(t, min_diff)

