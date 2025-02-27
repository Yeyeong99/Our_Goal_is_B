import sys
sys.stdin = open("input.txt", "r")

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(i, j, direction, idx, visited, current_sum):
    global max_sum
    if direction == 4:
        if i == idx[0][0] and j == idx[0][1]:
            max_sum = max(max_sum, current_sum)
            return
    else:
        # 범위 밖을 벗어남 or 같은 디저트
        if (i < 0 or N <= i) or (j < 0 or N <= j) or desserts[i][j] in visited:
            nx = i - dx[direction]
            ny = j - dy[direction]
            direction += 1
            before_idx = idx.pop()
            visited.pop()
            current_sum -= desserts[before_idx[0]][before_idx[1]]
        else:
            idx += [[i, j]]
            visited += [desserts[i][j]]
            current_sum += desserts[i][j]

            nx = i + dx[direction]
            ny = j + dy[direction]

            # 이미 방문한 카페로 되돌아 가는 경우 (Fig. 5)
            if nx != idx[0][0] and ny != idx[0][1] and [nx, ny] in idx:
                return

        dfs(nx, ny, direction, idx, visited, current_sum)




T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    max_sum = -float('inf')
    for x in range(N):
        for y in range(N):
            dfs(x, y, 0, [], [], 0)

    print(max_sum)