"""
파이프 옮기기
- N x N
- 1부터 행, 열 번호 시작
- 파이프
    - 2개의 연속된 칸을 차지하는 크기
    - 밀고 회전 가능 : 가로 세로 대각선
        - 45도만 회전 가능
    - 밀어서 이동 가능
    - 항상 빈칸만 차지
- 파이프 첫 위치 : (1, 1), (1, 2)
- 빈칸 : 0, 벽 : 1
- 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수
    - 이동 못하면 0
"""

# 파이프 타입 (가로1, 세로2, 대각선3) 찾는 함수
def find_type(s, e):
    pipe_type = (e[0]-s[0], e[1]-s[1])
    if pipe_type == (1, 1):
        return 2
    elif pipe_type == (0, 1):
        return 0
    elif pipe_type == (1, 0):
        return 1


def move_pipe(s, e):
    global answer

    # 파이프 타입 확인하기
    pipe_type = find_type(s, e)

    if e == (N-1, N-1):    # 목표지점을 만나면
        answer += 1    # 갈 수 있는 방법 추가
        return

    if e[0] >= N or e[1] >= N or e[0] < 0 or e[1] < 0:    # 범위를 넘어가면
        return

    if room[e[0]][e[1]] == 1:    # 벽이라면
        return
    if pipe_type == 2:    # 대각선이라면
        if room[e[0]-1][e[1]] == 1 or room[e[0]][e[1]-1] == 1:
            return

    if pipe_type == 2:    # 현재 파이프가 대각선이라면
        for next_type in [0, 1, 2]:
            ns = e
            ne = (e[0] + types[next_type][0], e[1] + types[next_type][1])
            move_pipe(ns, ne)

    elif pipe_type == 1:    # 세로 라면
        for next_type in [1, 2]:
            ns = e
            ne = (e[0] + types[next_type][0], e[1] + types[next_type][1])
            move_pipe(ns, ne)

    elif pipe_type == 0:    # 가로 라면
        for next_type in [0, 2]:
            ns = e
            ne = (e[0] + types[next_type][0], e[1] + types[next_type][1])
            move_pipe(ns, ne)


N = int(input())

room = [list(map(int, input().split())) for _ in range(N)]

answer = 0

start = (0, 0)
end = (0, 1)

types = [(0, 1), (1, 0), (1, 1)]    # 가로, 세로, 대각선

move_pipe(start, end)

print(answer)

