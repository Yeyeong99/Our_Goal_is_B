import sys

sys.stdin = open("input.txt", "r")


def subsets(arg_list):
    sub_sets = []
    for n in range(1 << len(arg_list)):
        sub_set = []
        for m in range(len(arg_list)):
            if n & (1 << m):
                sub_set.append((arg_list[m]))
        if sub_set and sub_set not in sub_sets:
            sub_sets.append(sub_set[:])
    return sub_sets


def find_max(arg_list):
    result = []
    for arg in arg_list:
        current_sum = 0
        if sum(arg) <= C:
            for a in arg:
                current_sum += a ** 2
            result.append(current_sum)
        else:
            current_sum += a ** 2
            result.append(current_sum)
    return result


T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    first_max = -float('inf')
    second_max = -float('inf')

    for i in range(N):
        for j in range(N - M + 1):
            current_honey = honeys[i][j: j + M]
            if min(current_honey) > C:
                break
            current_honey_sub = (subsets(current_honey))
            first_max = max(first_max, max(find_max(current_honey_sub)))

            for snd_i in range(i, N):
                for snd_j in range(0, N - M + 1):
                    if snd_i == i and snd_j < j + M:
                        continue
                    snd_select_honey_list = honeys[snd_i][snd_j: snd_j + M]
                    snd_sub = (subsets(snd_select_honey_list))
                    second_max = max(second_max, max(find_max(snd_sub)))

    print(first_max, second_max)
