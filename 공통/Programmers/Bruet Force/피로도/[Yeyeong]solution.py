def solution(k, dungeons):
    total_list = []

    def dfs(n, cnt, dungeons, visited):
        if len(visited) == n:
            total_list.append(visited[:])  # 새로운 리스트를 추가해야 함
            return

        for d in range(len(dungeons)):
            if dungeons[d] not in visited:
                visited.append(dungeons[d])  # 기존 리스트를 수정하지 말고 새로운 리스트를 사용
                dfs(n, cnt + 1, dungeons, visited)
                visited.pop()  # 백트래킹

    dfs(len(dungeons), 0, dungeons, [])
    max_num = -99999999
    numbers = 1
    for total in total_list:
        for i in range(len(dungeons) - 1):
            left = k - total[i][1]
            if total[i + 1][0] < left:
                numbers += 1
                initial = left
        max_num = max(numbers, max_num)
        numbers = 0
        initial = k
        
    return max_num 
