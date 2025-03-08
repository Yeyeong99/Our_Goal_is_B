# 1. 각 벌통에 있는 꿀의 양이 주어졌을 떄, 최대한 많은 수익을 얻으려고함.
# 2. 각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택, 두명의 일꾼은 선택 벌통 겹치면 안됨

from itertools import combinations

# 선택한 벌꿀 양 / 채취 꿀 최대 양 변수로 받음
# C를 넘지 않을 때 까지 제일 제일 적은 꿀 뺌
# C를 넘기지 않게 된다면 제곱 수입 계산

# 밑은 틀린 함수
# def honey_income(arr):
# #     global honey
# #
# #     new_arr = []
# #
# #     for i in range(len(arr)):
# #         new_arr.append(honey[arr[i][0]][arr[i][1]])
# #
# #     while sum(new_arr) > C:
# #         honey_min = new_arr[0]
# #         for i in new_arr:
# #             if i < honey_min:
# #                 honey_min = i
# #         new_arr.remove(honey_min)
# #     income = 0
# #
# #     for honey in new_arr:
# #         income += honey**2
# #     return income


def honey_income(arr):
    global honey

    new_arr = [honey[x][y] for x, y in arr]  # 벌꿀 양 리스트로 변환
    max_income = 0

    # 가능한 모든 부분 조합을 구해서 C 이하일 때 제곱합을 계산
    for r in range(1, len(new_arr) + 1):  # 최소 1개부터 최대 M개 선택
        for comb in combinations(new_arr, r):
            if sum(comb) <= C:
                max_income = max(max_income, sum(x ** 2 for x in comb))
    return max_income

# n*n 배열 / 선택 벌통 개수 / 꿀 정보 매개변수 받음
def choose(n, m):
    global result

    A_honey = 0  # 일꾼 A가 채취할 꿀 인덱스
    B_honey = 0  # 일꾼 B가 채취할 꿀 인덱스

    # 선택할 수 있는 벌통 종류 모든 케이스 구함
    every_case = []
    for i in range(n):
        for j in range(n - m + 1):
            case = []
            for num in range(m):
                case.append([i, j + num])
                # ex) case = [[0,1],[0,2],[0,3]]
            every_case.append(case)
            # ex) [[[0,1],[0,2],[0,3]] , .....

    for i in range(len(every_case)-1):
        A_honey = every_case[i]         # ex) [[0,1], [0,2], [0,3]]
        for j in range(i+1, len(every_case)):
            B_honey = every_case[j]
            value = 0
            honey_sum = 0
            for c in B_honey:
                if c in A_honey:
                    value = 1
                    break
            if value == 1:
                continue
            honey_sum = honey_income(A_honey)+honey_income(B_honey)
            if honey_sum > result:
                result = honey_sum





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, C = map(int,input().split())
    # N = 벌통들의 크기 / M = 선택할 수 있는 벌통의 개수 / C = 꿀을 채취할 수 있는 최대 양

    # N*N개 벌통에서 채취할 수 있는 꿀의 양에 대한 정보
    honey = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    choose(N,M)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
