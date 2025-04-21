"""
캐슬 디펜스
- 성을 향해 몰려오는 적을 잡는 턴 방식의 게임
- N x M
- 각 칸에는 최대 하나의 적만 존재할 수 있음.
- 궁수 3명 배치하기
    - 성이 있는 칸에 배치 가능, 최대 하나의 칸
    - 모든 궁수는 동시에 공격
    - 궁수는 적 하나 공격
    - 공격하는 적 : 거리가 D 이하인 적 중 가장 가까운 적
        - 여러 명일 경우, 가장 왼쪽에 있는 적 공격
        - 공격 받은 적은 게임 제외
        - 궁수의 공격이 끝나면 적은 이동함.
            - 한칸 아래로
            - 성이 있는 칸으로 이동한 경우, 게임 제외
            - 모든 적이 격자판에서 제외되면 게임 끝

- 궁수의 공격으로 제거할 수 있는 적의 최대 수 계산
"""

# 가장 가까운 적 없애는 함수
def kill_enemies(subset, matrix):
    total_die = 0
    # 적 없애기
    for turn in range(N):
        targets = set()
        # 궁수 찾기
        for arrow in subset:
            min_distance = (N + M)
            target = None
            # 적 찾기
            for r in range(N-1, -1, -1):
                for c in range(M):
                    if matrix[r][c] == 1:
                        distance = abs(N-r) + abs(arrow-c)
                        if distance <= D:
                            # 더 짧다면
                            if min_distance > distance:
                                min_distance = distance
                                target = (r, c)
                            elif min_distance == distance:
                                if target[1] > c:
                                    target = (r, c)
            # 나온 타겟 넣기
            if target:
                targets.add(target)

        if targets:
            # 나온 타겟 다 죽이기
            for tr, tc in targets:
                matrix[tr][tc] = 0
                total_die += 1    # 제거한 타겟 개수세기

        # 적들 한칸씩 내리기
        for r in range(N-1, -1, -1):
            for c in range(M):
                if matrix[r][c] == 1:
                    matrix[r][c] = 0
                    if r+1 < N:
                        matrix[r+1][c] = 1

    return total_die


# 궁수 위치 선정 함수
def arrow_positions(subset, start):
    global answer

    if len(subset) == 3:
        matrix = [row[:] for row in enemies]
        total_die = kill_enemies(subset, matrix)
        if answer < total_die:
            answer = total_die
        return

    for i in range(start, M):
        subset.append(i)
        arrow_positions(subset, i+1)
        subset.pop()



N, M, D = map(int, input().split())
enemies = [list(map(int, input().split())) for _ in range(N)]

# 궁수 자리 추가하기
enemies.append([0] * M)

answer = 0

arrow_positions([], 0)

print(answer)

