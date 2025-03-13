"""
[전력망을 둘로 나누기]
n개의 송전탑 - 하나의 트리 형태
전력망 네트워크를 2개로 분할
두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게
"""

def solution(n, wires):
<<<<<<< HEAD
    answer = n-1

    for i in range(n-1):
        adjust_list = [[0] for _ in range(n+1)]    # 인접리스트
        visited = [False]*(n+1)
        for idx, wire in enumerate(wires):
            v1, v2 = wire[0], wire[1]
            if idx != i:
                adjust_list[v1].append(v2)
                adjust_list[v2].append(v1)
        cnt = 0

        def dfs(n):
            nonlocal cnt

            stack = []
            stack.append(n)
            visited[n] = True

            while stack:
                current = stack.pop()

                for v in adjust_list[current]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        cnt += 1
        dfs(1)

        tower1 = cnt
        tower2 = n - cnt
        gap = abs(tower2 - tower1)

        answer = min(answer, gap)

=======
    answer = -1
    adjust_list = [[] for _ in range(n+1)]    # 인접리스트
    
    for v1, v2 in wires:
        adjust_list[v1].append(v2)
        adjust_list[v2].append(v1)
        
    print(adjust_list)

    visited = [False]*(n+1)    # 방문했는지 확인하는
    
    # 인접한 곳이 가장 많은 노드 찾기
    max_len = 0
    
    for i in range(1, n+1):
        if max_len < len(adjust_list[i]):
            max_len = len(adjust_list[i])
            max_v = i
    
    cnt = 0

    # 탐색 >> 가장 인접한 곳이 많은 곳을 나눈다.
    def dfs(i, subset):
        if i == len(adjust_list[max_v]):
            return
        
        if len(subset) == len(adjust_list[max_v])-1:
            for v in adjust_list[max_v]:
                if v in subset:
                    pass
                
            return
        
        visited[i] = True
        dfs(0, subset+[adjust_list[max_v][i]])
        
        visited[i] = False
        dfs(i+1, subset)
                    
>>>>>>> f6d22e028b872e4d90dd31f6e0132a197202c156
    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
<<<<<<< HEAD

print(solution(n, wires))
=======
solution(n, wires)
>>>>>>> f6d22e028b872e4d90dd31f6e0132a197202c156
