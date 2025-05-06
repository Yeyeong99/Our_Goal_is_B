"""
치킨 배달
- N x N
- 빈칸, 치킨집, 집
- (r, c) -> (1, 1) 부터 시작
- 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
    - 집을 기준
    - 각각의 집은 치킨 거리를 가지고 있음.
    - 도시의 치킨 거리 = sum(치킨 거리)

- 0: 빈칸, 1: 집, 2: 치킨집
- 이 도시에서 가장 수익을 많이 낼 수 있는 치킨 집의 개수 : M
- 도시에 있는 치킨 집 중 최대 M개 >> 나머지 폐업
- 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지..
"""
def find_house(matrix, target_number):
    targets = []
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == target_number:
                targets.append((i, j))
    
    return targets


# 치킨 거리 구하는 함수
def cal_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


def dfs(subset, start):
    global answer
    
    if len(subset) == M:
        
        total_dist = 0
        for house in houses:
            min_chicken_dist = 2*N
            for live in subset:
                current_dist = cal_distance(house, live)
                if current_dist < min_chicken_dist:
                    min_chicken_dist = current_dist
            
            total_dist += min_chicken_dist
        
        if total_dist < answer:
            answer = total_dist
            
        return
    
    for s in range(start, len(chickens)):
        dfs(subset+[chickens[s]], s+1)


N, M = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(N)]

answer = 52 * (N ** 2)

# 1. 치킨집 찾기
chickens = find_house(cities, 2)

# 2. 그냥 집 구하기
houses = find_house(cities, 1)

# 3. 그 중 M개 구하기 + 최소 거리 계산하기
dfs([], 0)

print(answer)
