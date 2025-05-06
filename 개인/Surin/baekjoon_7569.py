"""
[토마토]
- M * N * H
- 잘 익은 것도 있고, 아직 익지 않은 것도 있고
- 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
    - 인접하다 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    - 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
- 며칠이 지나면 다 익을까?
    - 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력
"""
from collections import deque

# 안익은 토마토 찾기
def is_riped():
    global tomatoes
    
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 0:    # 안익은 토마토가 있다면
                    return False
    return True


# 처음부터 익은 토마토 부터 bfs
def bfs():
    global tomatoes, visited
    
    queue = deque()
    
    # 토마토가 익은 칸을 찾기기
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 1:    # 익은 토마토라면
                    queue.append((h, n, m))
                    visited[h][n][m] = 1    # 익었다는 표시해주기
    
    while queue:    # 리스트가 빌 때까지
        ch, cn, cm = queue.popleft()

        for d in range(6):     # 여섯 방향으로 돌꺼니깐
            nh, nn, nm = ch + dz[d], cn + dy[d], cm + dx[d]
            if (0 <= nh < H) and (0 <= nn < N) and (0 <= nm < M):    # 범위 안에 있다면
                if tomatoes[nh][nn][nm] == 0:    # 안 익은 토마토가 있는지 확인하기
                    if visited[nh][nn][nm] == 0:    # 방문하지 않았다면면
                        queue.append((nh, nn, nm))    # 리스트에 추가해주고
                        visited[nh][nn][nm] = visited[ch][cn][cm] + 1    # 익었다는 표시해주기
                        tomatoes[nh][nn][nm] = tomatoes[ch][cn][cm] + 1
                        
    return visited[ch][cn][cm]-1
                

# 상자의 크기
M, N, H = map(int, input().split())

# 3차원
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방문 기록 확인용
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

# 델타 설정
dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]   
dz = [0, 0, 0, 0, 1, -1]

answer = bfs()    # 토마토 익히기

if not is_riped():
    answer = -1
    
print(answer)