def solution(n, wires):
    def save_first(idx):
        if not visited[idx]:
            visited[idx] = 1
            first.append(idx)
            if tree[idx]:
                for num in tree[idx]:
                    save_first(num)

    min_difference = float('inf')
    # 순회를 돌면서 각 경우 간선을 안 이음
    # 그럴 때마다 나눠지는 두 그룹을 구함
    for i in range(n - 1):
        tree = [[] for _ in range(n + 1)]
        left = wires[: i] + wires[i + 1:]  # 현재 간선 제외 나머지
        tree[wires[i][0]] = [wires[i][0]]  # 현재 간선은 그냥 자기 자신 저장
        # 나머지 간선에 대해 트리 생성
        for wire in left:
            tree[wire[0]].append(wire[1])
            tree[wire[1]].append(wire[0])

        # 분리된 노드 수 구하기
        for t in range(n + 1):  # 첫 번째로 순회할 노드 구하기
            if tree[t]:
                first_idx = t
                break
        first = []
        visited = [0] * (n + 1)
        save_first(first_idx)
        difference = abs((n - len(first)) - len(first))

        min_difference = min(min_difference, difference)

    return min_difference
