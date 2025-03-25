# 게임 맵의 상태 : maps
# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값?
# 도착불가할 경우 -1
# 0 : 벽이 있음 / 1 : 벽이 없음
# 처음 >> (0, 0) / 끝 >> (n-1, m-1)
# n x m 크기
from collections import deque

def bfs(arr, start, visited, delta, N, M):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    
    while queue:
        current = queue.popleft()
        
        for di, dj in delta:
            ni, nj = current[0] + di, current[1] + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1 and arr[ni][nj]:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[current[0]][current[1]] + 1
                    
    return visited[N-1][M-1]
        
        
def solution(maps):
    
    answer = 0
    
    N, M = len(maps), len(maps[0])
    
    start = (0, 0)
    # end = (N-1, M-1)
    visited = [[-1] * M for _ in range(N)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    answer = bfs(maps, start, visited, delta, N, M)
    
    return answer
