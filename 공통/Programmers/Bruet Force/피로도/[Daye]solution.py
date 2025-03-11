# XX게임에는 피로도 시스템( 0 이상 정수 표현) 이 있다
# 피로도 사용해서 던전 탐험
# 탐험을 시작하기 위해 필요한 "최소 필요 피로도", 탐험을 마쳤을 때 소모되는 '소모 피로도'
# 유저가 최대한 많은 던전을 탐험할 수 있게
# k = 유저 현재 피로도 / dungeons ( 던전별 최소 필요 피로도, 소모피로도)

# 문제 해결 : 만들어 질 수 있는 던전 모든 순서를 순열로 구하고 그 순서대로 돌면서 몇개의 던전을 탐색할 수 있는지 구함
# 모든 경우의 수를 구함

from itertools import permutations

def solution(k, dungeons):

    max_explore = 0

    dungeon_order = list(permutations(dungeons, len(dungeons)))
    for dungeon_list in dungeon_order:
        go = 0
        copy_k = k                  # k를 복사를 안해주면 k 값이 갱신이 돼서 던전 하나의 순서만 확인함
        for d in dungeon_list:
            if copy_k >= d[0]:
                copy_k -= d[1]
                go += 1
        if go > max_explore:
            max_explore = go
    return max_explore


