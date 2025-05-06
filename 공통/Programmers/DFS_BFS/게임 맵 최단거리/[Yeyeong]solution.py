def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N = len(maps)
    M = len(maps[0])
    from collections import deque
    def bfs(i, j, cnt):
        queue = deque()
        queue.append((i, j, cnt))
        visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
        while queue:
            x, y, dist = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx == N - 1 and ny == M - 1:
                    return dist
                if nx >= N or nx < 0 or ny < 0 or ny >= M:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] == 0:
                    continue
                    
                visited[nx][ny] = 1
                queue.append((nx, ny, dist + 1))
                
    answer = bfs(0, 0, 2)
    if answer == None:
        answer = -1
    return answer
