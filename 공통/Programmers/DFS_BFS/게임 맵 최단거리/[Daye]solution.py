# 프로그래머스 문제 : 게임 맵 최단거리
# 상대 팀 진영 최단 거리 도착하기 문제
# bfs 활용

from collections import deque

dy = [ 0, 1, 0, -1]
dx = [ 1, 0, -1, 0 ]


def bfs(row,col,maps):

    # 행 * 열
    N = len(maps)
    M = len(maps[0])

    p = deque()
    p.append((row,col))
    visited = [[0] * M for _ in range(N)]
    visited[row][col] = 1

    while p:
        y, x = p.popleft()

        # 도착 지점 도착했으면 다른 곳은 볼 필요가 없음
        if y == N-1 and x == M-1:
            break

        # 델타 탐색
        for d in range(4):

            ny = y + dy[d]
            nx = x + dx[d]

            # 이동 인덱스 범위 벗어나면 안되고 방문한 적 없어야하고 벽이 아니여야함
            if 0 <= ny < N and  0 <= nx < M and visited[ny][nx] == 0 and maps[ny][nx] != 0:
                p.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1

    # 도착지점에 갈 수 있을경우
    if visited[N-1][M-1] > 0:
        short = visited[N-1][M-1]

    # 도착지점 못 갔을경우
    else:
        short = -1

    return short

def solution(maps):

    # bfs 시작인덱스 넣음
    answer = bfs(0,0,maps)

    return answer


