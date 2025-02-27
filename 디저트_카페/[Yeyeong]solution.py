import sys
sys.stdin = open("input.txt", "r")


def dfs(i, j, direction, idx, visited, current_sum):
    global max_sum
    if direction == 4:
        if i == idx[0][0] and j == idx[0][1]:
            max_sum = max(max_sum, current_sum)
            return
    else:
        if (i < 0 or N <= i) and (j < 0 or N <= j):
            return

        idx += [[i, j]]
        visited += [desserts[i][j]]
        current_sum += desserts[i][j]

        if direction == 0:
            nx = i + 1
            ny = j + 1
        elif direction == 1:
            nx = i + 1
            ny = j - 1
        elif direction == 2:
            nx = i - 1
            ny = j - 1
        elif direction == 3:
            nx = i - 1
            ny = j + 1

        # 이미 방문한 카페로 되돌아 가는 경우 (Fig. 5)
        if nx != idx[0][0] and ny != idx[0][1] and [nx, ny] in idx:
            return
        # 좌표는 다르지만 같은 종류의 디저트를 파는 경우
        if desserts[nx][ny] in visited:
            return

        dfs(nx, ny, idx, visited, current_sum)

        idx = []
        visited = []
        current_sum = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_sum = -float('inf')
    for x in range(N):
        for y in range(N):
            dfs(x, y, 0, [], [], 0)

    print(max_sum)