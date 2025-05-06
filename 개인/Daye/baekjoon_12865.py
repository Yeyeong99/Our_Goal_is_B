# 백준 12865 파이썬

# N : 여행에 필요하다고 생각하는 물건 N개
# W : 물건의 무게
# V : 물건의 가치
# V만큼 즐길 수 있음
# 최대 K 무게만을 넣을 수 있는 배낭만 들고 다님
# 최대한 즐거운 여행을 하ㅣ 위해 배낭에 넣을 수 있는 물건들의 가치 최댓값
# 최댓값 구하기!!

# 완탐 DFS
# 시간 초과 났음

def dfs(idx, w, v):
    global happy

    # 모든 물품을 확인했으면 최고 가치 갱신
    if idx >= N:
        if v > happy:
            happy = v

    elif w <= K:
        w += items[idx][0]
        # 현재 고른 물건을 골랐을 경우
        if w <= K:
            dfs(idx + 1 , w, v + items[idx][1])
        # 현재 고른 물건을 안 골랐을 경우
        w -= items[idx][0]
        dfs(idx + 1, w, v)

# 물건 수 / 담을 수 있는 최대 무게
N, K = map(int,input().split())

# N개 물건들의 물건 무게 W / 물건 가치 V 가 주어짐
items = [list(map(int,input().split())) for _ in range(N)]
happy = 0

# item 시작 인덱스, 담은 물건 무게 , 가치 합
dfs(0,0, 0)

print(happy)