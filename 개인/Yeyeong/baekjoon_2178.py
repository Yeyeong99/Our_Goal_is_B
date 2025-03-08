dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, distance, visited):
    global min_distance
    if i == N - 1 and j == M - 1:
        min_distance = min(min_distance, distance)

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and [nx, ny] not in visited:
                visited += [[nx, ny]]
                distance += 1
                dfs(nx, ny, distance, visited)
                distance -= 1
                visited.pop()


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

min_distance = float('inf')

dfs(0, 0, 1, [[0, 0]])

print(min_distance)