# 다리를 최대한 많이 지을 수 있는 경우의 수 구하는 게 포인트
# 서쪽 게이트는 무조건 써야하는것임
# 완탐 모든 경우의 수 구하기.

# 서로 겹쳐지지 않는 다리 인지 체크

# 다리 연결
def dfs(bridge,west_idx,east_idx):
    global can
    # 서쪽 게이트 길이 만큼 bridge가 채워진다면 이제 겹쳐지는지 체크
    if len(bridge) == W:
        can += 1
        return

    for j in range(east_idx,E):
        bridge.append([west_idx,j])
        dfs(bridge,west_idx+1,j+1)
        bridge.pop()

T = int(input())
for tc in range(1,T+1):
    W, E = map(int,input().split())                     # W는 서쪽 게이트 / E는 동쪽 게이트

    west = []
    east = []

    can = 0

    # 서쪽 게이트 번호 수 리스트 생성
    for i in range(W):
        west.append(i+1)

    # 동쪽 게이트 번호 수 리스트 생성
    for i in range(E):
        east.append(i+1)

    dfs([],0, 0)

    print(can)

# 사실상 서쪽 동쪽 리스트 게이트 생성한거 의미없는 행동이엿음... W, E 범위로 받으면되니까
# 리스트를 만드니 append, pop 등 불필요한 연산이 지속되는겨..