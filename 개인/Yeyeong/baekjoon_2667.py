from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, visit):
    queue = deque()
    numbers = 0
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        numbers += 1

        if not visit[x][y]:
            visit[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (nx < 0 or N <= nx) or (ny < 0 or N <= ny):
                    continue
                if (nx, ny) in queue:
                    continue
                if visit[nx][ny]:
                    continue
                if houses[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
    return numbers


N = int(input())
houses = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

houses_result = []
for q in range(N):
    for p in range(N):
        if houses[q][p] and not visited[q][p]:
            current_houses = bfs(q, p, visited)
            houses_result.append(current_houses)

houses_result.sort()
print(len(houses_result))
for h in houses_result:
    print(h)
