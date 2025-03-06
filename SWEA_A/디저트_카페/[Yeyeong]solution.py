import sys
sys.stdin = open("input.txt", "r")
# 방향: 5시가 0 7시가 1 10시가 2 2시가 3 > 사각형을 만들기 위해 이 순서로 움직임
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, N, d, idx, visited, current_sum):
    global max_sum

    if idx:  # idx 는 방문한 idx 저장
        if [i, j] == idx[0] and d == 3:  # 방향이 3인 상황에서 첫 번째 idx 를 만났을 경우
            max_sum = max(max_sum, current_sum)  # 업데이트
            return
        elif [i, j] in idx:  # 방문한 idx 면 종료
            return
        elif i < idx[0][0]:  # 가지치기 - 엉뚱한 곳(첫 idx보다 높은 곳)으로 가면 종료
            return
    if visited:  # 디저트 종류 저장
        if [i, j] not in idx and desserts[i][j] in visited:  # 간 적은 없는데 종류는 같으면
            return  # (간 적 없다고 안하면 -> 첫 번째 방문 노드도 이 조건에 걸림)

    idx += [[i, j]]
    visited += [desserts[i][j]]
    current_sum += 1

    # 이동은 두 가지 -> 0, 1 / 1, 2 / 2, 3 / 3, 0 이런 식으로 진행됨
    nx = dx[d] + i
    ny = dy[d] + j

    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, N, d, idx, visited, current_sum)

    d += 1
    d %= 4
    nx = dx[d] + i
    ny = dy[d] + j

    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, N, d, idx, visited, current_sum)

    idx.pop()
    visited.pop()
    current_sum -= 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    dots = [[0, 0], [0, N - 1], [N - 1, 0], [N - 1, N - 1]]  # 꼭지점 저장 > 나중에 제외
    max_sum = -1

    for x in range(N):
        for y in range(N):
            if [x, y] not in dots:  # 꼭지점 제외
                dfs(x, y, N, 0, [], [], 0)

    print(f"#{t} {max_sum}")
