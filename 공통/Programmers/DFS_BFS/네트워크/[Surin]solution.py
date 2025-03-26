from collections import deque


def find_group(n, arr):
    queue = deque()
    visited = [False] * n
    group_cnt = 0

    for start in range(n):
        if not visited[start]:
            queue.append(start)
            visited[start] = True

            while queue:
                current = queue.popleft()

                for member in range(n):
                    if arr[current][member]:  # 서로 연결되어 있으면
                        if not visited[member]:  # 방문한 적이 없으면
                            queue.append(member)
                            visited[member] = True

            group_cnt += 1

    return group_cnt


def solution(n, computers):
    answer = find_group(n, computers)
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))