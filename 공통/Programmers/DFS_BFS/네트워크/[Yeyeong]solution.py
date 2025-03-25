def solution(n, computers):
    nodes = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                nodes[i].append(j)
                nodes[j].append(i)
    
    def dfs(node):
        nonlocal visited
        if not visited[node]:
            visited[node] = 1
            for next_node in nodes[node]:
                dfs(next_node)
            
    visited = [0] * n
    answer = 0
    
    for k in range(n):
        if not visited[k]:
            dfs(k)
            answer += 1
    return answer
