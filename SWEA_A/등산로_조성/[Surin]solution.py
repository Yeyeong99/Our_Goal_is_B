# 가장 높은 곳의 높이 찾는 함수
def find_max_heights(arr, n):
    max_height = 0
    for i in range(n):
        for j in range(n):
            max_height = max(max_height, arr[i][j])

    return max_height


# 가장 높은 곳의 인덱스 찾는 함수
def find_highest_idx(arr, n):
    idx_list = []

    max_h = find_max_heights(arr, n)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_h:
                idx_list.append([i, j])

    return idx_list


# 안 깎고 이동시키기
def dfs(move, i, j, k, si, sj):
    global max_move

    visited[i][j] = True   # 방문한 곳 넣는 리스트
    
    # 갈 수 있는 곳 찾아보기
    for di, dj in delta:
        if (0 <= i+di < N) and (0 <= j+dj < N):    # 배열 안에 있다면

            if visited[i+di][j+dj]:    # 이미 방문했던 위치면
                continue

            if mountain[i][j] > mountain[i+di][j+dj]:    # 현재 위치보다 낮다면
                visited.append([i, j])
                # 이동
                dfs(move+1, i+di, j+dj, k, i, j)
                continue

            if mountain[i+di][j+dj] - k < mountain[i][j]:    # 현재 위치에 +K를 한 것이 옮길 곳보다 크다면
                x = mountain[i+di][j+dj] - (mountain[i][j] - 1)
                mountain[i+di][j+dj] -= x
                visited.append([i, j])
                dfs(move+1, i+di, j+dj, 0, i, j)
                mountain[i+di][j+dj] += x

    # 재귀 종료 조건 : 더이상 갈곳이 없을 때
    max_move = max(max_move, move)
    visited[i][j] = False    # 방문했던 거 다시 돌려놓기
    return



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 한 변의 길이, 최대 공사 가능 깊이
    N, K = map(int, input().split())
    # 지형 정보
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 지형들 찾기
    highest_locations = find_highest_idx(mountain, N)

    max_move = 1

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    visited = [[False]*N for _ in range(N)]
    
    for i, j in highest_locations:
        dfs(1, i, j, K, i, j)

    print(f'#{tc} {max_move}')