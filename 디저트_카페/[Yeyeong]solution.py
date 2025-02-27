import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, result):
    global max_sum
    if idx:
        max_sum = max(max_sum, result)
        return
    else:
        result += desserts[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                dfs(nx, ny, result)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_sum = -float('inf')