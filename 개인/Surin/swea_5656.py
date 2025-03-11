from collections import deque


# 공을 놓을 위치 찾기
def dfs(c, subset_list):  # 현재의 열 번호

    if c == W:  # 너비까지 왔다면 돌아가기
        return

    # 종료조건
    if sum(visited) == N:  # 위치를 다 찾았다면
        # 벽돌을 깨기
        blocks_copy = [block[:] for block in blocks]  # 원래 배열은 복구해야 하니깐 복사해서 사용함.

        for col in subset_list:  # 찾은 열 조합을 반복한다.
            for row in range(H):  # 해당 열에서 1 이상인 숫자가 있는 행을 찾는다.
                if blocks_copy[row][col] != 0:  # 뭔가 있으면
                    ti, tj = row, col
                    break  # 멈춘다.

            # 깨기 시작
            crush_blocks(ti, tj, blocks_copy)

            # 아래로 내려주기
            move_down(blocks_copy)

        # 남아있는 벽돌수 찾기
        find_min(blocks_copy)
        # print(subset_list)
        return

    # 업데이트
    visited[c] += 1
    dfs(0, subset_list + [c])

    visited[c] -= 1
    dfs(c + 1, subset_list)


# 벽돌 깨기 => bfs!
def crush_blocks(si, sj, arr):
    queue = deque()
    queue.append([si, sj])

    while queue:  # 큐 안에 요소가 있을 때까지
        ci, cj = queue.popleft()

        if blocks[ci][cj] == 1:
            arr[ci][cj] = 0

        if blocks[ci][cj] > 1:
            arr[ci][cj] = 0
            for d in range(4):  # 상하좌우 확인하기
                for k in range(blocks[ci][cj]):  # 벽돌 안의 숫자 - 1 거리만큼 터트릴 수 있음.

                    ni, nj = ci + delta[d][0] * k, cj + delta[d][1] * k

                    if (0 <= ni < H) and (0 <= nj < W):  # 범위에 있으면
                        if blocks[ni][nj] >= 1:  # 1 이상이면
                            if arr[ni][nj] != 0:
                                queue.append([ni, nj])  # queue에 넣어주기


# 아래로 내려주는 작업
def move_down(arr):
    for j in range(W):
        new_numbers = []  # 1 이상의 숫자 넣을 리스트
        for i in range(H - 1, -1, -1):  # 뒤에서부터 확인하기
            if arr[i][j] >= 1:  # 1 이상이면
                new_numbers.append(arr[i][j])

        if len(new_numbers) < H:  # 모자라다면
            new_numbers.extend([0] * (H - len(new_numbers)))  # 0 더 채워주기

        for i in range(H):
            arr[H - 1 - i][j] = new_numbers[i]


# 남아있는 벽돌 수 찾기
def find_min(arr):
    global min_cnt

    cnt = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] > 0:
                cnt += 1

    min_cnt = min(min_cnt, cnt)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    # 구슬을 쏠 수 있는 횟수, 가로, 세로
    N, W, H = map(int, input().split())
    # 벽돌의 배열
    blocks = [list(map(int, input().split())) for _ in range(H)]

    # 상하좌우 델타
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    visited = [0] * W  # 방문 가로

    min_cnt = W * H

    dfs(0, [])

    print(f'#{tc} {min_cnt}')