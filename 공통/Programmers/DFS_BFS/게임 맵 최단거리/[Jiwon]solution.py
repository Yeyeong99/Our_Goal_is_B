from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        now_x, now_y, cnt = queue.popleft()

        if now_x == N-1 and now_y == M-1:
            return cnt

        for d in range(4):
            new_x = now_x + di[d]
            new_y = now_y + dj[d]

            if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == -1 and maps[new_x][new_y] == 1:
                queue.append((new_x, new_y, cnt + 1))
                visited[new_x][new_y] = cnt + 1

    return -1
