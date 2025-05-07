from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']


def bfs(i, j, d, current_keys):
    queue = deque()
    queue.append((i, j, d, current_keys))
    while queue:
        c_x, c_y, c_d, key = queue.popleft()
        if maps[c_x][c_y] == '1':
            return c_d + 1
        if maps[c_x][c_y] in keys and maps[c_x][c_y] not in key:
            key.append(maps[c_x][c_y])
        for k in range(4):
            nx = c_x + dx[k]
            ny = c_y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maps[nx][ny] == '#':
                continue
            if maps[nx][ny] in doors:
                if maps[nx][ny].lower() not in key:
                    continue

            queue.append((nx, ny, c_d + 1, key))


for n in range(N):
    for m in range(M):
        if maps[n][m] == '0':
            result = bfs(n, m, 0, [])

if result == None:
    print(-1)
else:
    print(result)