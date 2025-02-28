import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, cnt, dis, way):
    global max_distance
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if [nx, ny] in way:
            continue
        if 0 <= nx < N and 0 <= ny < N:  # 범위 안에 있음
            original = [nx, ny, maps[nx][ny]]

            if maps[i][j] <= maps[nx][ny]:  # 이동할 경로의 높이가 현재 인덱스의 높이 보다 같거나 큼
                # 깎을 수 있는 기회가 있음, 이동할 경로의 높이와 현재 인덱스 높이의 차가 깎아낼 수 있는 범위 내에 있음
                if cnt == 1 and maps[nx][ny] - maps[i][j] <= K:
                    cnt = 0
                    for k in range(maps[nx][ny] - maps[i][j] + 1, K + 1):
                        dis += 1
                        maps[nx][ny] -= k
                        way.append([nx, ny])
                        dfs(nx, ny, cnt, dis, way)
                        dis -= 1
                        maps[original[0]][original[1]] = original[2]
                        way.pop()
                    cnt = 1
                else:
                    # for x_, y_ in way:
                    #     print(cnt, [x_, y_], maps[x_][y_], end=" ")
                    # print()
                    max_distance = max(max_distance, dis)
                    continue
            else:
                way.append([nx, ny])
                dis += 1
                dfs(nx, ny, cnt, dis, way)
                way.pop()
                dis -= 1
        else:
            continue


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]

    peak = max([max(m) for m in maps])

    max_distance = -float('inf')
    distance = 1
    counts = 1
    for x in range(N):
        for y in range(N):
            if maps[x][y] == peak:
                dfs(x, y, counts, distance, [[x, y]])

    print(f"#{t} {max_distance}")