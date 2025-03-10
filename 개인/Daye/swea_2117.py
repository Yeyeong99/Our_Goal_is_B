# swea 홈 방범 서비스

from collections import deque

# BFS 기반 거리 계산
def bfs(si, sj):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    visited[si][sj] = 1  # 시작점 거리 0
    q.append((si, sj))

    while q:
        xi, xj = q.popleft()

        for d in range(4):  # 상하좌우 이동
            ni = xi + dx[d]
            nj = xj + dy[d]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[xi][xj] + 1
                q.append((ni, nj))
    return visited

# 수익 계산 함수
def profit(arr, k):
    global max_houses

    # 운영 비용 계산
    cost = k * k + (k - 1) * (k - 1)

    # 서비스 제공받는 집 개수 계산
    provide = sum(1 for hi, hj in home if arr[hi][hj] <= k)

    total_profit = (provide * M) - cost

    # 손해를 보지 않는 경우, 최대 집 개수 갱신
    if total_profit >= 0:
        max_houses = max(max_houses, provide)

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N 도시 크기 / M 하나의 집이 지불할 수 있는 비용
    city = [list(map(int, input().split())) for _ in range(N)]

    max_houses = 0  # 최대 서비스 제공 가능한 집 개수 초기화

    dx = [0, 1, 0, -1]  # 방향 벡터 (상하좌우)
    dy = [1, 0, -1, 0]

    # 집 위치 저장
    home = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]

    # 모든 좌표(i, j)에서 BFS 실행
    for i in range(N):
        for j in range(N):
            range_map = bfs(i, j)  # BFS 탐색 실행

            for k in range(1, N + 5):  # K는 최대 N+1까지 가능
                profit(range_map, k)  # 현재 K 범위에서 수익 계산

    print(f"#{test_case} {max_houses}")  # 최대 서비스 제공 가능한 집 개수 출력
