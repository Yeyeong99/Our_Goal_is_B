# 백준 17135 캐슬디펜스
# 지피티랑 같이 품..............거의 다 풀어준거같음..........................어렵다.....................................

# 게임 진행 N * M 격자판
# 격자판 N + 1 행 모든 칸에는 성이 있음
# 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산

from itertools import combinations
from collections import deque
# 궁수 공격 범위에 적이 있는지 확인

# 왼쪽, 위,오른쪽
di = [0, -1, 0]
dj = [-1, 0, 1]
def bfs(start_i,start_j,graph):

    visited=  [[False] * M for _ in range(N)]

    q = deque()
    q.append((start_i,start_j,1))
    visited[start_i][start_j] = True

    while q:
        i, j, dist = q.popleft()

        if dist > D:
            return None

        # 적 발견 시 해당 위치 반환
        if i < N and graph[i][j] == 1:
            return (i,j)

        for d in range(3):
            ni, nj = i + di[d] , j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni,nj, dist+1))

    return None

def move_enemy(graph):

    for i in range(N-1,0,-1):
        graph[i] = graph[i-1][:]
    graph[0] = [0] * M

def game_start(game_map,archer):
    # 원본 맵 복사
    temp_map = [row[:] for row in game_map]
    # 현재 조합에서 죽인 적 수
    cnt = 0

    while True :

        # 궁수들이 동시에 쏠 수 있는 적의 위치들
        # 동시에 같은 적을 죽일 수 있기에 집합 사용
        enemys = set()

        for col in archer:
            enemy = bfs(N-1,col,temp_map)
            if enemy:
                enemys.add(enemy)

        # 적 제거
        for i, j in enemys:
            if temp_map[i][j] == 1:
                temp_map[i][j] = 0
                cnt += 1

        # 적 이동 (한 칸씩 아래로)
        move_enemy(temp_map)

        # 맵에 적이 하나도 없음
        if sum(map(sum,temp_map)) == 0:
            break

    return cnt

# N 행 / M 열 / D 궁수 공격 거리 제한
N, M, D = map(int,input().split())

# N * M 격자판 배치
game = [list(map(int,input().split())) for _ in range(N)]


# 궁수 배치
archers = list(combinations(range(0,M),3))

# 최대 킬 반영

result = 0

origin = [row[:] for row in game]


# 궁수 조합 마다 게임 실행
for archer in archers:
    copied_game = [row[:] for row in origin]

    result = max(result, game_start(copied_game, archer))

print(result)
