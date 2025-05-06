def solution(k, dungeons):
    max_num = 0  # 최대로 돌 수 있는 던전 개수 저장

    def dfs(current_k, dungeons, visited_count):
        nonlocal max_num
        max_num = max(max_num, visited_count)  # 최댓값 갱신

        for i in range(len(dungeons)):
            if dungeons[i] is None:  # 이미 방문한 던전 건너뜀
                continue
            min_req, consume = dungeons[i]

            if current_k >= min_req:  # 던전을 돌 수 있는 경우만 진행
                dungeons[i] = None  # 방문 처리
                dfs(current_k - consume, dungeons, visited_count + 1)  # 체력 차감 후 다음 탐색
                dungeons[i] = (min_req, consume)  # 원상 복구 (백트래킹)

    dfs(k, dungeons, 0)
    return max_num
