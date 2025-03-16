from collections import deque


def count_nodes(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count


def solution(n, wires):
    min_diff = float('inf')

    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i + 1:]  # 하나의 간선을 제거

        graph = {i: [] for i in range(1, n + 1)}
        for v1, v2 in temp_wires:
            graph[v1].append(v2)
            graph[v2].append(v1)

        sub_tree_size = count_nodes(graph, temp_wires[0][0], n)
        diff = abs((n - sub_tree_size) - sub_tree_size)
        min_diff = min(min_diff, diff)

    return min_diff
