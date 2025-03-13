from collections import deque
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
 
def bfs(i, j):
    queue = deque([(i, j, 1)])
    start_room = nums[i][j]
    max_dist = 1
 
    while queue:
        x, y, dist = queue.popleft()
 
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
 
            if 0 <= nx < N and 0 <= ny < N and nums[nx][ny] == nums[x][y] + 1:
                queue.append((nx, ny, dist + 1))
                max_dist = max(max_dist, dist + 1)
 
    return start_room, max_dist
 
 
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
 
    max_distance = 0
    initial = float('inf')
 
    for x in range(N):
        for y in range(N):
            start, dist = bfs(x, y)
 
            if dist > max_distance:
                max_distance = dist
                initial = start
            elif dist == max_distance:
                initial = min(initial, start)
 
    print(f"#{t} {initial} {max_distance}")
