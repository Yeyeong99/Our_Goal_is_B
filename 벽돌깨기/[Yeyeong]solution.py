import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def explosion(i, j, block, visited, total):
    bomb = block[i][j]
    for d in range(4):
        for b in range(bomb):
            nx = i + dx[d] * b
            ny = j + dy[d] * b

            if 0 <= nx < H and 0 <= ny < W:  # 델타 탐색이 범위 안에 존재
                if [nx, ny] not in visited:  # 방문 하지 않은 좌표
                    if block[nx][ny] >= 1:  # 벽돌이 1보다 큰 수인 경우 - 다른 벽돌 깨기
                        original = [nx, ny]
                        total += 1  # 깨진 벽돌 수 저장
                        visited += [original]
                        explosion(nx, ny, block, visited, total)
                        blocks[original[0]][original[1]] = 0
                        visited.pop()

    # 깨진 벽돌을 아래로 옮기는 작업
    for m in range(W):
        for n in range(1, H):
            if block[m][n - 1] == 0:  # 아래 있는 숫자가 0 이면
                value = block[m][n]
                block[m][n - 1] = value  # 현재 값을 아래로 옮기고
                block[m][n] = 0  # 현재 값은 0으로 업데이트

    return block, total, visited


def dfs(i, j, block, cnt, total):
    global max_blocks
    if cnt == N:
        max_blocks = max(max_blocks, total)
        return
    else:
        blocks_copy = [b[:] for b in block]
        current_sum = 0

        if block[i][j] != 0:
            block, total, visited = explosion(i, j, block, [], total)

            cnt += 1
            dfs(i, j, block, cnt, total)
            cnt -= 1
            block = blocks_copy


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    blocks = list(map(list, zip(*blocks[::-1])))

    max_blocks = -float('inf')

    counts = 1
    for w in range(W - 1):
        for h in range(H - 1, -1, -1):
            dfs(w, h, blocks, counts, 0)
