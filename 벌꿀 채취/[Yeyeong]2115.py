import sys

sys.stdin = open("input.txt", "r")

# 선택할 벌통의 인덱스, 여태까지 선택한 벌통의 이익, 벌통의 합


def dfs(honey_idx, honey_benefit, honey_sum):
    global part_sum

    # 백트래킹, 여태까지 선택한 꿀의 합이 C를 넘으면 이득을 알 필요가 없음
    if honey_sum > C: return

    # 선택할 벌통이 M에 도달하면 최대값 갱신
    if honey_idx == M:
        part_sum = max(part_sum, honey_benefit)

    cnt_sum = honeys[i][j + honey_idx]
    cnt_benefit = honeys[i][j + honey_idx] ** 2

    # 현재 꿀을 선택 함
    dfs(honey_idx + 1, honey_benefit + cnt_benefit, honey_sum + cnt_sum)

    # 현재 꿀을 선택 안함
    dfs(honey_idx + 1, honey_benefit, honey_sum)


T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N):
        for j in range(N - M + 1):
            part_sum = 0

            dfs(0, 0, 0)
            fst_max = part_sum

            for snd_i in range(i, N):
                for snd_j in range(0, N - M + 1):
                    if snd_i == i and snd_j < j + M:
                        continue
                    part_sum = 0
                    dfs(snd_i, snd_j, 0)
                    snd_max = part_sum
                    max_sum = max(max_sum, fst_max + snd_max)
