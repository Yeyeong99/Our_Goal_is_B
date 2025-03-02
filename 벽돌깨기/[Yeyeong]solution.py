import sys
from itertools import product

sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def explosion(i, j, visited):  # 벽돌 깨기
    global blocks
    bomb = blocks[i][j]
    blocks[i][j] = 0

    for d in range(4):
        for b in range(1, bomb):
            nx = i + dx[d] * b
            ny = j + dy[d] * b

            if 0 <= nx < W and 0 <= ny < H:  # 델타 탐색이 범위 안에 존재
                if [nx, ny] not in visited:  # 방문 하지 않은 좌표
                    if blocks[nx][ny] >= 1:  # 벽돌이 0이 아닌 경우
                        visited += [[nx, ny]]
                        explosion(nx, ny, visited) # 다른 벽돌 깨러 가기


def gravity():  # 벽돌이 깨졌을 때 아래로 떨어 지는 함수
    global blocks
    for width in range(W):  # 오른 쪽으로 90도 회전한 상태
        left_blocks = []
        for height in range(H - 1, -1, -1):
            # 가장 아래 있으면서 0이 아닌 경우, 0이 아니고 나보다 아래에 0이 있는 경우
            if blocks[width][height] != 0 or (0 in blocks[width][:height] and height == 0):
                left_blocks.append(blocks[width][height])
                blocks[width][height] = 0
        if left_blocks:  # 슬라이싱으로 내려줌
            blocks[width][: len(left_blocks)] = left_blocks[::-1]


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    blocks = list(map(list, zip(*blocks[::-1])))
    possible_w = [list(range(W))] * N

    # N 개의 열을 고르는 경우의 수 모음 (0, 0, 0), (0, 0, 1) 이런 식
    possible_ws = list(product(*possible_w))

    min_blocks = float('inf')

    # 경우의 수를 모두 순회 하며 벽돌 깨기
    for ws in possible_ws:
        blocks_copy = [_[:] for _ in blocks]
        for w in ws:
            for h in range(H - 1, -1, -1):
                if blocks[w][h] != 0:
                    explosion(w, h, [])
                    gravity()
                    break  # 벽돌 하나 깼으면 다음 경우로 넘어감

        # 한 경우의 수를 모두 수행 (예 - (0, 0, 0)의 경우를 모두 깸) - 남은 벽돌 세기
        current_block = sum([1 for r in range(W) for c in range(H) if blocks[r][c] != 0])
        # 블록 업데이트
        min_blocks = min(min_blocks, current_block)
        # 블록이 남은 게 없으면 계산 더 안하게 함
        if min_blocks == 0:
            break
        # 블록을 직접 핸들링 했으므로 원상 복귀
        blocks = blocks_copy
    print(f"#{t} {min_blocks}")

