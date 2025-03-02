
def dfs(i, j, kind, d):
    global start
    global result
    di = [1, 1, -1, -1,100]
    dj = [-1, 1, 1, -1,100]

    if d > 3:
        return

    if d == 3 and i == start[0] and j == start[1]:
        if len(kind) > result:
            result = len(kind)
            return

    for num in range(d, d+2):
        if 0 <= i + di[num] < N and 0 <= j + dj[num] < N:
            if dessert[i + di[num]][j + dj[num]] not in kind:
                kind.append(dessert[i + di[num]][j + dj[num]])
                dfs(i + di[num], j + dj[num], kind, num )
                kind.pop()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                    # N*N 사각형

    dessert = [list(map(int,input().split())) for _ in range(N)]

    dessert_kind = []

    result = -1

    delta = 0

    for row in range(N-2):
        for col in range(1, N-1):
            start = (row,col)
            dfs(row,col,dessert_kind, delta)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
