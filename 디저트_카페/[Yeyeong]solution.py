import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, idx, result, current_sum):
    global max_sum
    if len(idx) >= 2:
        if i == idx[0][0] and j == idx[0][1]:
            max_sum = max(max_sum, current_sum)
            return
    else:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= N:
                continue
            if ny < 0 or ny >= N:
                continue
            if nx == idx[-1][0]:
                continue
            if ny == idx[-1][1]:
                continue
            if nx != idx[0][0] and ny != idx[0][1] and desserts[nx][ny] in result:
                continue

            current_sum += desserts[nx][ny]
            idx += [[nx, ny]]
            result += [desserts[nx][ny]]
            dfs(nx, ny, idx, result, current_sum)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_sum = -float('inf')
    for x in range(N):
        for y in range(N):
            dfs(x, y, [[x, y]], [desserts[x][y]], desserts[x][y])

    print(max_sum)