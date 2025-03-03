import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, N, d, idx, visited, current_sum):
    global max_sum

    if idx:
        if [i, j] == idx[0] and d == 3:
            max_sum = max(max_sum, current_sum)
            return
        elif [i, j] in idx:
            return
    if visited:
        if [i, j] not in idx and desserts[i][j] in visited:
            return

    idx += [[i, j]]
    visited += [desserts[i][j]]
    current_sum += 1

    nx = dx[d] + i
    ny = dy[d] + j

    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, N, d, idx, visited, current_sum)

    d += 1
    d %= 4
    nx = dx[d] + i
    ny = dy[d] + j

    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, N, d, idx, visited, current_sum)

    idx.pop()
    visited.pop()
    current_sum -= 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    dots = [[0, 0], [0, N - 1], [N - 1, 0], [N - 1, N - 1]]  # 모서리 저장 > 나중에 제외
    max_sum = -1

    for x in range(N):
        for y in range(N):
            if [x, y] not in dots:
                dfs(x, y, N, 0, [], [], 0)

    print(f"#{t} {max_sum}")
