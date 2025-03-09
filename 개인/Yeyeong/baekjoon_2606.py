def dfs(node, visit):
    global total
    if not visit[node]:
        visit[node] = True
        total += 1
        if computers[node]:
            for c in computers[node]:
                dfs(c, visited)


N = int(input())
M = int(input())
computers = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

total = 0
visited = [False] * (N + 1)
dfs(1, visited)

print(total - 1)