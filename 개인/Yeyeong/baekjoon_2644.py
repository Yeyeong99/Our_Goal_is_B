from collections import deque

N = int(input())
fst_person, snd_person = map(int, input().split())

M = int(input())

family = [[] for _ in range(N + 1)]
for _ in range(M):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)  # 부모-자식 관계는 양방향 그래프


def find_family_bfs(N, fst, snd):
    queue = deque([(fst, 0)])  # (현재 노드, 촌수)
    visited = [False] * (N + 1)
    visited[fst] = True  # 시작 노드 방문 처리

    while queue:
        current, count = queue.popleft()

        if current == snd:
            return count  # 촌수 반환

        for next_person in family[current]:
            if not visited[next_person]:
                visited[next_person] = True
                queue.append((next_person, count + 1))  # 촌수 +1

    return -1  # 관계 없음


print(find_family_bfs(N, fst_person, snd_person))