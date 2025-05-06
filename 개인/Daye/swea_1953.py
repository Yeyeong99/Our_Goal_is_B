# 큐 쓸때 제발!!!!!!!!!!!!pop(0)하자!!!!!!!!!!!아니면 deque를 쓰던가!!!!!!!!!!!!!!!!!!!!!!!!

def bfs(si,sj):
    global result

    visited = [[0] * M for i in range(N)]
    q = []
    q.append([si,sj])
    visited[si][sj] = 1

    while q:
        ti, tj = q.pop(0)

        # 델타 우/하/좌/상  0 1 2 3
        for delta in range(4):
            ni = ti + di[delta]
            nj = tj + dj[delta]

            if 0<= ni < N and 0 <= nj < M:
                # 파이프 1는 상,하,좌,우
                if underground[ti][tj] == 1:

                    if delta == 0 and underground[ni][nj] in right:
                        if visited[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 1 and underground[ni][nj] in down:
                        if visited[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 2 and underground[ni][nj] in left:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 3 and underground[ni][nj] in up:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1

                # 파이프 2는 상,하
                if underground[ti][tj] == 2:
                    if delta == 1 and underground[ni][nj] in down:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 3 and underground[ni][nj] in up:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                # 파이프 3은 좌,우
                if underground[ti][tj] == 3:
                    if delta == 0 and underground[ni][nj] in right:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 2 and underground[ni][nj] in left:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                # 파이프 4는 우,상
                if underground[ti][tj] == 4:
                    if delta == 0 and underground[ni][nj] in right:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 3 and underground[ni][nj] in up :
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                # 파이프 5는 하,우
                if underground[ti][tj] == 5:
                    if delta == 1 and underground[ni][nj] in down:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 0 and underground[ni][nj] in right:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                # 파이프 6은 하, 좌
                if underground[ti][tj] == 6:
                    if delta == 1 and underground[ni][nj] in down:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 2 and underground[ni][nj] in left:
                        if visited[ni][nj] == 0 :
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                # 파이프 7은 좌,상
                if underground[ti][tj] == 7:
                    if delta == 2 and underground[ni][nj] in left:
                        if visited[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1
                    if delta == 3 and underground[ni][nj] in up:
                        if visited[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = visited[ti][tj] + 1

    for i in range(N):
        for j in range(M):
            if 0< visited[i][j] <= L:
                result += 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, R, C, L = map(int,input().split())                    # N 세로 , M 가로, R 맨홀 뚜껑 행 인덱스 , C 열 인덱스 , L 탈촐 시간

    underground = [list(map(int,input().split())) for _ in range(N)]    # 지하 터널 지도 정보

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    up = [1, 2, 5, 6]       # 상
    down = [1, 2, 4, 7]     # 하
    left = [1, 3, 4, 5]     # 좌
    right = [1, 3, 6, 7]    # 우ㅡ

    result = 0

    bfs(R, C)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
