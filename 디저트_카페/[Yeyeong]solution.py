import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, direction, idx, result, current_sum):
    global max_sum
    if direction == 4:
        if i == idx[0][0] and j == idx[0][1]:
            max_sum = max(max_sum, current_sum)
            return
    else:
        if direction == 0:
            if 0 <= i + 1 < N and 0 <= j + 1 < N:
                idx += [[i + 1, j + 1]]
                result += [desserts[i + 1][j + 1]]
                current_sum += desserts[i + 1][j + 1]
                dfs(i + 1, j + 1, 0, idx, result, current_sum)
            elif i + 1 >= N or j + 1 >= N:
                idx += [[i + 1, j - 1]]
                result += [desserts[i + 1][j - 1]]
                current_sum += desserts[i + 1][j - 1]
                dfs(i + 1, j - 1, 1, idx, result, current_sum)
        elif direction == 1:
            if 0 <= i + 1 < N and 0 <= j - 1 < N:
                idx += [[i + 1, j - 1]]
                result += [desserts[i + 1][j - 1]]
                current_sum += desserts[i + 1][j - 1]
                dfs(i + 1, j - 1, 1, idx, result, current_sum)
            elif i + 1 >= N or j - 1 < N:
                idx += [[i - 1, j - 1]]
                result += [desserts[i - 1][j - 1]]
                current_sum += desserts[i - 1][j - 1]
                dfs(i - 1, j - 1, 2, idx, result, current_sum)

        elif direction == 2:
            if 0 <= i - 1 < N and 0 <= j - 1 < N:
                idx += [[i - 1, j - 1]]
                result += [desserts[i - 1][j - 1]]
                current_sum += desserts[i - 1][j - 1]
                dfs(i - 1, j + 1, 2, idx, result, current_sum)
            elif i - 1 < 0 or j - 1 > N:
                idx += [[i - 1, j + 1]]
                result += [desserts[i - 1][j + 1]]
                current_sum += desserts[i - 1][j + 1]
                dfs(i - 1, j - 1, 3, idx, result, current_sum)

        elif direction == 3:
            if 0 <= i - 1 < N and 0 <= j + 1 < N:
                idx += [[i - 1, j + 1]]
                result += [desserts[i - 1][j + 1]]
                current_sum += desserts[i - 1][j + 1]
                dfs(i - 1, j + 1, 3, idx, result, current_sum)
            elif i - 1 < 0 or j - 1 > N:
                idx += [[i - 1, j - 1]]
                result += [desserts[i - 1][j - 1]]
                current_sum += desserts[i - 1][j - 1]
                dfs(i - 1, j - 1, 4, idx, result, current_sum)

        idx = []
        result = []
        current_sum = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_sum = -float('inf')
    for x in range(N):
        for y in range(N):
            dfs(x, y, 0, [[x, y]], [desserts[x][y]], desserts[x][y])

    print(max_sum)