N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
queue = [(0, 0)]

while queue:
    i, j = queue.pop(0)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if maze[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                queue.append([ni, nj])
print(visited[N-1][M-1] + 1)