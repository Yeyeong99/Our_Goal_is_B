import heapq
 
# 거리 구하는 함수
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Prim 알고리즘
def prim(start_node):
    pq = [(0, start_node)]    # 가중치, 노드 번호
    total_cost = 0

    while pq:
        cost, now = heapq.heappop(pq)
        if visited[now]:    # 방문 했다면
            continue    # 건너뛰기

        visited[now] = True
        total_cost += cost

        # 다음 노드 구하기
        for next_cost, next_node in graph[now]:
            if not visited[next_node]:    # 방문하지 않았다면
                # 우선순위 큐에 넣어주기
                heapq.heappush(pq, (next_cost, next_node))

    return total_cost


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 콘센트 개수
    N = int(input())

    # 콘센트 리스트
    points = []

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    # 누전 차단기까지 고려 (주어진 순서대로 콘센트 간다.)
    visited = [False] * (N+1)

    # 인접 리스트
    graph = [[] for _ in range(N+1)]

    # 콘센트끼리 거리 계산 해주기
    for i in range(N-1):
        for j in range(i+1, N):
            dist = manhattan(points[i], points[j])
            # 거리, 끝점
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    # 콘센트와 누전 차단기 거리 계산 (누전 차단기를 N번 노드로 간주한다.)
    for i in range(N):
        dist = manhattan(points[i], (0, 0))
        graph[i].append((dist, N))
        graph[N].append((dist, i))

    # prim 알고리즘 시작하기
    answer = prim(N)    # 누전 차단기에서 시작하기

    print(f'#{tc} {answer}')
