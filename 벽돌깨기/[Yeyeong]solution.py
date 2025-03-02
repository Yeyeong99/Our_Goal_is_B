import sys
from itertools import product

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def explosion(i, j, visited):
    global blocks
    bomb = blocks[i][j]
    blocks[i][j] = 0

    for d in range(4):
        for b in range(1, bomb):
            nx = i + dx[d] * b
            ny = j + dy[d] * b

            if 0 <= nx < H and 0 <= ny < W:  # 델타 탐색이 범위 안에 존재
                if [nx, ny] not in visited:  # 방문 하지 않은 좌표
                    if blocks[nx][ny] >= 1:  # 벽돌이 1보다 큰 수인 경우 - 다른 벽돌 깨기
                        visited += [[nx, ny]]
                        explosion(nx, ny, visited)


def gravity():
    global blocks
    for h in range(H - 1):
        for w in range(W):
            if blocks[h][w] != 0 and blocks[h + 1][w] == 0:
                blocks[h][w], blocks[h + 1][w] = blocks[h + 1][w], blocks[h][w]


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    blocks_copy = [w[:] for w in blocks]
    possible_w = [list(range(W))] * N

    possible_ws = list(product(*possible_w))

    min_blocks = float('inf')

    for ws in possible_ws:
        for h in range(H):
            for w in ws:
                if blocks[h][w] != 0:
                    explosion(h, w, [])
                    gravity()
            current_block = sum([1 for r in range(H) for c in range(W) if blocks[r][c] != 0])
            min_blocks = min(min_blocks, current_block)
            blocks = blocks_copy

    print(min_blocks)

