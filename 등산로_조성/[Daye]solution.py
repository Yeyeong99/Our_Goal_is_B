
#import sys
#sys.stdin = open("input.txt", "r")

# 봉우리 높이 지도, 제일 높은 봉우리 인덱스가 시작, 최대 공사 깊이 , 자르는 횟수, 등산로 길이 cnt 매개변수로 받음
def dfs(map_info, p, k, cut, road):

    # print (map_info)
    dy = [0, 1, 0, -1]                             # 행 이동
    dx = [1, 0, -1, 0]                             # 열 이동

    delta = list(zip(dy, dx))                      # 델타
    # [ [0, 1], [1, 0], [0, -1], [-1,0] ]

    lowest = map_info[p[0]][p[1]]

    for d in delta:                                # dfs 돌때마다 현지점이 제일 낮으면 일단 등산로 길이 추가
        ny = p[0] + d[0]
        nx = p[1] + d[1]

        if not (0 <= ny < N and 0 <= nx < N):
            continue

        if lowest > map_info[ny][nx]:
            lowest = map_info[ny][nx]

    if lowest == map_info[p[0]][p[1]]:
        roads.append(road)

    for d in delta:
        ny = p[0] + d[0]
        nx = p[1] + d[1]
        if 0 <= nx < N and 0 <= ny < N:                         # 일단 이동 방향이 지정 범위에 있어야함
            if map_info[p[0]][p[1]] > map_info[ny][nx]:
                save = map_info[p[0]][p[1]]                     # 왔던 곳 못간다고 지정하기전에 그 값 저장
                map_info[p[0]][p[1]] = MAX_H                    # 왔던 곳은 다시 못감
                road += 1
                dfs(map_info, [ny, nx], k, cut, road)
                road -= 1
                map_info[p[0]][p[1]] = save

            if map_info[p[0]][p[1]] <= map_info[ny][nx]:
                if cut == 1 and (map_info[p[0]][p[1]] + k > map_info[ny][nx]):
                    save = map_info[p[0]][p[1]]
                    save_cut = map_info[ny][nx]
                    map_info[ny][nx] = map_info[p[0]][p[1]] - 1  # 갈 방향 봉우리 높이를 현재 위치보다 1 낮게 만듬
                    cut = 0                                      # 이제 공사 불가능
                    road += 1
                    map_info[p[0]][p[1]] = MAX_H  # 왔던 곳은 다시 못감
                    dfs(map_info, [ny, nx], k, cut, road)
                    cut += 1
                    road -= 1
                    map_info[p[0]][p[1]] = save
                    map_info[ny][nx] = save_cut

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N, K = map(int,input().split())                # 지도 한 변의 길이 N / 최대 공사 가능 깊이 K
    MAX_H = 30
    map_information = [list(map(int,input().split())) for _ in range(N)]        # 지도 정보

    result = []                                                     # 가장 긴 등산로 길이
    peak = 0                                                        # 제일 높은 봉우리 높이
    peaks = []                                                      # 제일 높은 봉우리들
    cut_cnt = 1                                                     # 봉우리를 깎을 수 있는 횟수
    roads = []                                                      # 등산로 길이들 리스트
    road_start = 1                                                  # 등산로 시작 cnt

    # 제일 높은 봉우리 높이 찾음.
    for i in range(N):
        for j in range(N):
            if map_information[i][j] > peak:
                peak = map_information[i][j]
    # 제일 높은 봉우리 인덱스 찾음.
    for i in range(N):
        for j in range(N):
            if map_information[i][j] == peak:
                peaks.append([i, j])

    for start in peaks:
        dfs(map_information, start, K, cut_cnt, road_start)  # 제일 긴 등산로 값 받음

    # print(roads)
    result = max(roads)

    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////


# 코드 문제점 : bfs 만약에 원래 정보를 바꾸는 일이 있으면 bfs 안으로 들어가고 나서 무조건 다시 원래 정보 바꾼 곳을 다시 원래대로 돌려야함.