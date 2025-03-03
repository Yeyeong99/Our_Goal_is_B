import sys

sys.stdin = open("input.txt", "r")

from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]

    # 첫 번째 꿀  선택
    firsts = []
    for n in range(N):
        for m in range(N - M + 1):
            first = honeys[n][m: m + M]
            if max(first) <= C:
                fst_totals = []
                for k in range(1, M + 1):
                    fst_totals += list(combinations(first, k))
                firsts += [[n, range(m, m + M), first, fst_totals]]

    # 두 번째 꿀 선택
    total_sum = -float('inf')
    for i, js, first, first_total in firsts:
        if M * 2 > N:  # 같은 행에서 선택 못하는 경우 - 다음 행으로 범위 조정
            start = i + 1
        else:
            start = i
        for n in range(start, N):
            for m in range(N - M + 1):
                snd_totals = []
                if M * 2 > N:  # 같은 행에서 채취 못할 때 다음 행에서 채취
                    second = honeys[n][m: m + M]
                    if max(second) <= C:
                        for k in range(1, M + 1):
                            snd_totals += list(combinations(second, k))
                else:  # 같은 행에서 채취 가능할 때
                    if i != n and range(m, m + M) != js:  # 첫 번째 꿀의 인덱스와 다를 경우
                        second = honeys[n][m: m + M]
                        if max(second) <= C:
                            for k in range(1, M + 1):
                                snd_totals += list(combinations(second, k))
                # 첫 번째 꿀의 최대
                fst_sum = -float('inf')
                for fst in first_total:
                    if sum(fst) <= C:
                        current_sum = sum([num ** 2 for num in fst])
                        fst_sum = max(fst_sum, current_sum)

                # 두 번째 꿀의 최대
                snd_sum = -float('inf')
                for snd in snd_totals:
                    if sum(snd) <= C:
                        current_sum = sum([num ** 2 for num in snd])
                        snd_sum = max(current_sum, snd_sum)
                total_sum = max(total_sum, fst_sum + snd_sum)
    print(f"#{t} {total_sum}")
