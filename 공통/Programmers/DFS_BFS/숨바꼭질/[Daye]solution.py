# 백준 1697 숨바꼭질
# BFS 문제 최단거리는 DFS 말고 BFS로 접근하는게 맞음. DFS는 깊이가 너무 깊어질때 재귀 너무 많이해서 런타임 에러남 

from collections import deque

def bfs():

    pq = deque()
    pq.append([N,0])
    visited = [0] * 1000001

    while pq:
        now, dist = pq.popleft()
        visited[now] = 1

        if now == K:
            return dist

        for next in [now+1,now-1,now*2]:
            if 0 <= next <= 100000 and visited[next] != 1:
                pq.append([next,dist+1])

# N = 수빈이 위치 / K = 동생 위치
N, K = map(int,input().split())

min_cnt = 1e9

result = bfs()

print(result)