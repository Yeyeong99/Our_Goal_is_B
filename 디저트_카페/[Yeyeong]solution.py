import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, d, ds, idx, visited, current_sum):
    global max_sum
    if idx:
        if [i, j] == idx[0]:
            max_sum = max(max_sum, current_sum)

    if visited:
        if desserts[i][j] in visited:
            return

    idx += [[i, j]]
    visited += [desserts[i][j]]
    current_sum += 1

    d %= 4
    nx = dx[d] + i
    ny = dy[d] + j

    if 0 <= nx < N and 0 <= ny < N:
        ds += [d]
        dfs(nx, ny, d, ds, idx, visited, current_sum)
        ds.pop()

    if ds[0] == 0:
        d += 1
        d %= 4
        nx = dx[d] + i
        ny = dy[d] + j

        if 0 <= nx < N and 0 <= ny < N:
            ds += [d]
            dfs(nx, ny, d, ds, idx, visited, current_sum)
            ds.pop()

        d = 4 * 0 + d
        d -= 1
        idx.pop()
        visited.pop()
        current_sum -= 1

    elif ds[0] == 1:
        if d == 0:
            d = 4
        d -= 1

        nx = dx[d] + i
        ny = dy[d] + j

        if 0 <= nx < N and 0 <= ny < N:
            ds += [d]
            dfs(nx, ny, d, ds, idx, visited, current_sum)
            ds.pop()

        d = 4 * 0 + d
        d += 1
        idx.pop()
        visited.pop()
        current_sum -= 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    dots = [[0, 0], [0, N - 1], [N - 1, 0], [N - 1, N - 1]]
    max_sum = -1
    for x in range(N):
        for y in range(N):
            if [x, y] not in dots:
                dfs(x, y, 0, [], [], [], 0)

    print(max_sum)