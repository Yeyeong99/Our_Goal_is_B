from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy, 0, 0))  # x, y, distance, key_bitmask
    visited[sx][sy][0] = True

    while queue:
        x, y, dist, keys = queue.popleft()

        if maps[x][y] == '1':
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            cell = maps[nx][ny]
            if cell == '#':
                continue

            new_keys = keys
            if 'a' <= cell <= 'f':
                new_keys |= (1 << (ord(cell) - ord('a')))
            if 'A' <= cell <= 'F':
                if not (keys & (1 << (ord(cell) - ord('A')))):
                    continue

            if not visited[nx][ny][new_keys]:
                visited[nx][ny][new_keys] = True
                queue.append((nx, ny, dist + 1, new_keys))
    return -1

for i in range(N):
    for j in range(M):
        if maps[i][j] == '0':
            print(bfs(i, j))
