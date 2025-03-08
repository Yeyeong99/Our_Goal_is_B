import sys

sys.stdin = open("input.txt", "r")


def dfs(x, y, way, cases, time):
    global total_case
    time -= 1

    if time == 0:
        total_case += cases
        return
    tunnel = matrix[x][y]
    for r, c in tunnels[tunnel]:
        nx = x + r
        ny = y + c
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] != 0 and [nx, ny] not in way:
                next_tunnel = matrix[nx][ny]
                if [0 - r, 0 - c] in tunnels[next_tunnel]:
                    cases += 1
                    way += [[nx, ny]]
                    dfs(nx, ny, way, cases, time)
                    way.pop()



T = int(input())

tunnels = {
    1: [[1, 0], [-1, 0], [0, -1], [0, 1]],
    2: [[1, 0], [-1, 0]],
    3: [[0, -1], [0, 1]],
    4: [[-1, 0], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[1, 0], [0, -1]],
    7: [[-1, 0], [0, -1]]
}

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    total_case = 0

    dfs(R, C, [[R, C]], 1, L)

    print(total_case)