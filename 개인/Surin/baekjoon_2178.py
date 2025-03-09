"""
[미로 탐색]
- N x M
- 1 : 이동 가능한 칸
- 0 : 이동 불가능한 칸

- (0, 0)에서 출발 ~ (N, M)까지 도착
- 지나야 하는 최소 칸 수
- 상하좌우로만 움직이기 가능
"""
def bfs(si, sj):
    queue = []
    queue.append([si, sj])
    visited[si][sj] += 1
    
    while queue:
        ci, cj = queue.pop(0)    # 현재의 좌표
        
        if ci == N-1 and cj == M-1:
            return visited[ci][cj]
        
        for di, dj in delta:
            ni, nj = di + ci, dj + cj
            if (0 <= ni < N) and (0 <= nj < M):    # 범위 안에 있다면
                if maze[ni][nj] == 1 and visited[ni][nj] == 0:    # 갈 수 있는 곳이라면
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[ci][cj] + 1


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]    # 방문 여부 확인 리스트

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

answer = bfs(0, 0)

print(answer)