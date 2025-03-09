def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    visited = [False] * N   # 방문여부 확인 리스트

    def dfs(i, stress, total):    # stress : 현재의 피로도, total : 지금까지 다녀간 던전
        nonlocal answer, N
        
        answer = max(answer, total)
    
        if i == N:    # 모든 던전을 다 돌았다면
            return
        
        # 조건 만족하면
        if not visited[i]:
            if (dungeons[i][1] <= stress) and (dungeons[i][0] <= stress):     # 최소 필요 피로도 조건도 만족하고, 소모 피로도 보다도 남은 피로도가 크면
                visited[i] = True    # 방문 O
                dfs(0, stress-dungeons[i][1], total+1)
                visited[i] = False    # 백트래킹

        # 조건 만족하지 않으면
        dfs(i+1, stress, total)    # 다음으로 넘어가기
     
    dfs(0, k, 0)    
    
    return answer