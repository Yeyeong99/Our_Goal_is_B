"""
[물놀이를 가자]
- 지도 : N * M
- i, j
- 물 : W / 땅 : L
- 물인 칸으로 이동하기 위한 최소 이동 횟수의 합은?
"""
from collections import deque

def calculate_sum(dist_map):
    return sum(sum(cell for cell in row if cell != -1) for row in dist_map)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def find_water():
    for i in range(N):
        for j in range(M):
            if info[i][j] == 'W':
                queue.append((i, j, 0))
                visited[i][j] = 0

def bfs():
    global answer

    while queue:
        ci, cj, distance = queue.popleft()

        for d in range(4):
            ni, nj = ci + dy[d], cj + dx[d]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1:
                    queue.append((ni, nj, distance+1))
                    visited[ni][nj] = distance + 1


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 지도 크기
    N, M = map(int, input().split())

    # 정보
    info = [list(input().strip()) for _ in range(N)]

    visited = [[-1] * M for _ in range(N)]

    queue = deque()
    
    find_water()
    bfs()

    print(f'#{tc} {calculate_sum(visited)}')

from collections import deque


def multi_source_bfs(N, M, grid):
    # 방향 벡터 (상, 우, 하, 좌)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 거리를 저장할 2D 배열 초기화
    dist = [[-1] * M for _ in range(N)]
    queue = deque()

    # 모든 물(W) 위치를 큐에 추가하고 거리를 0으로 초기화
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                queue.append((i, j))
                dist[i][j] = 0

    # BFS 실행
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 그리드 범위 내이고, 아직 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    # 모든 땅(L)까지의 거리 합 계산
    total_distance = sum(dist[i][j] for i in range(N) for j in range(M) if grid[i][j] == 'L')

    return total_distance


# 테스트 케이스 처리
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    result = multi_source_bfs(N, M, grid)
    print(f'#{tc} {result}')
