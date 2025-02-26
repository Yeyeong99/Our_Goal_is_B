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

    stack = []
    for i in range(N):
        for j in range(N - M + 1):
            current_honey = []
            idx = []
            for k in range(M):
                current_honey.append(honeys[i][j + k])
                idx.append([i, j + k])
            if min(current_honey) > C:
                break

            if not stack:
                stack.append(current_honey)
            else:
                last_in = stack[-1]
                last_in_sub = (subsets(last_in))
                current_honey_sub = (subsets(current_honey))
                if max(find_max(last_in_sub)) <= max(find_max(current_honey_sub)):
                    stack.pop()
                    stack.append(current_honey)
                    honeys[i][j + k] = 0
    print(stack)
