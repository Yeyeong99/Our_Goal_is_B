dx = [1, 1, 1]
dy = [-1, 0, 1]


def dfs(i, j, fuel, distance, direction):
    global min_fuel
    if fuel >= min_fuel:
        return
    if distance == n:
        min_fuel = min(min_fuel, fuel)
        return
    else:
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if direction == k:
                continue

            dfs(nx, ny, fuel + fuels[nx][ny], distance + 1, k)


n, m = map(int, input().split())

fuels = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
min_fuel = float('inf')
for i in range(n):
    for j in range(m):
        dfs(i, j, fuels[i][j], 1, -1)

print(min_fuel)

