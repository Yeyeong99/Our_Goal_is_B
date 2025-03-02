import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def explosion(i, j, block, visited):
    global total
    bomb = block[i][j]
    block[i][j] = 0

    for d in range(4):
        for b in range(1, bomb):
            nx = i + dx[d] * b
            ny = j + dy[d] * b

            if 0 <= nx < H and 0 <= ny < W:  # 델타 탐색이 범위 안에 존재
                if [nx, ny] not in visited:  # 방문 하지 않은 좌표
                    if block[nx][ny] >= 1:  # 벽돌이 1보다 큰 수인 경우 - 다른 벽돌 깨기
                        original = [nx, ny]
                        visited += [original]
                        total += 1  # 깨진 벽돌 수 저장
                        explosion(nx, ny, block, visited)


def gravity(block, W, H):
    # 깨진 벽돌을 아래로 옮기는 작업
    for m in range(W):
        for n in range(1, H):
            if block[m][n - 1] == 0:  # 아래 있는 숫자가 0 이면
                value = block[m][n]
                block[m][n - 1] = value  # 현재 값을 아래로 옮기고
                block[m][n] = 0  # 현재 값은 0으로 업데이트


def dfs(i, j, block, cnt):
    global max_blocks, total
    if cnt == N:
        max_blocks = max(max_blocks, total)
        print(max_blocks)
        cnt = 1
        total = 0
    else:
        blocks_copy = [b[:] for b in block]
        current_sum = 0

        if block[i][j] == 1:
            block[i][j] = 0
        elif block[i][j] > 1:
            explosion(i, j, block, [])

        cnt += 1
    block = blocks_copy


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    blocks = list(map(list, zip(*blocks[::-1])))

    max_blocks = -float('inf')

    counts = 0
    total = 0
    for w in range(W - 1):
        for h in range(H - 1, -1, -1):
            dfs(w, h, blocks, counts)
    print(max_blocks)