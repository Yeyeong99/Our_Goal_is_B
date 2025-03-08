from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0, 1)])  # 첫 번째 좌표, 거리
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y, distance = queue.popleft()

        if x == N - 1 and y == M - 1:
            return distance

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx >= N or nx < 0) or (ny < 0 or ny >= M):
                continue
            if maze[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny, distance + 1))


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

print(bfs())