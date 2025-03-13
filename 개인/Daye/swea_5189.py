# 전자카트 ( 완전탐색 )
#
# import sys
# sys.stdin = open("input.txt", "r")

# 문제 포인트 : 사무실에서 출발해서 관리 구역을 돌고 다시 사무실로 와야함
# 각 구역을 한번씩만 방문하고 최소 배터리 사용량을 구해야함

def dfs(j, v, hap, move):
    global min_electricity

    # 백트래킹
    if hap > min_electricity:
        return

    for c in range(N):

        # 마지막 이동일 때 합 비교 하고 최소합 갱신
        if move == N-1:
            hap += electricity[j][c]
            if hap < min_electricity:
                min_electricity = hap

        # 이동하려고 하는 구역이 가본 적 없는 곳, 지금 구역 이닐 때만 이동 가능
        elif v[c][0] == 0 and j != c:
            hap += electricity[j][c]
            v[j] = [1] * N
            move += 1
            dfs(c, v, hap, move)
            hap -= electricity[j][c]
            v[j] = [0] * N
            move -= 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                    # N * N
    electricity = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    min_electricity = 1e9

    # [0][0]은 지금 구역 -> 지금 구역 이므로 아예 제외함
    for col in range(1, N):
        visited[0] = [1] * N
        dfs(col, visited, electricity[0][col], 1)
        visited[0] = [0] * N

    print(f"#{test_case} {min_electricity}")
    # ///////////////////////////////////////////////////////////////////////////////////
