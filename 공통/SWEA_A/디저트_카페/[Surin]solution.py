def dfs(i, j, d, arr, fi, fj):
    global max_cnt
    
    if d == 4:    # 델타 인덱스가 끝났으면
        return
    
    # 재귀 종료 조건 1 : 만약 2차원 배열을 넘어갔다면
    if not((0 <= i < N) and (0 <= j < N)):    
        return
    
    # 재귀 종료 조건 2 : 방문 기록이 있다면
    if visited[i][j]:
        if i == fi and j == fj:    # 그런데 첫 번째 위치라면 (재귀 종료와 결과 도출 조건 : 처음 위치로 돌아왔다면)
            max_cnt = max(max_cnt, len(arr))    # 여기까지의 길이 비교하기
            return
        else:    # 첫 번째 위치 아니면
            return    # 그냥 리턴하기
    
    # 재귀 종료 조건 3 : 칸의 수가 이미 존재한다면
    if cafes[i][j] in arr:
        return
    
    # 델타의 순서는 계속 0 > 1 > 2 > 3으로 진행
    # 이동 가능한 경우 : 델타 인덱스 0에서 다시 탐색 시작
    arr.append(cafes[i][j])    # 숫자 리스트에 추가
    visited[i][j] = True    # 방문 완료
    dfs(i+delta[d][0], j+delta[d][1], d, desserts, fi, fj)
    
    # 이동 불가능한 경우
    visited[i][j] = False
    arr.pop()
    dfs(i, j, d+1, desserts, fi, fj)
    

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    
    # 대각선으로 갈 델타
    delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    
    # 방문 여부 확인 배열
    visited = [[False]*N for _ in range(N)]
    
    # 디저트 종류별로 넣는 곳
    desserts = []
    
    # 디저트 최대 종류
    max_cnt = 0
    
    # 시작점 잡아주기
    for i in range(N-1):
        for j in range(1, N):
            dfs(i, j, 0, desserts, i, j)
    
    # 돌 수 있는 카페가 없었다면
    if max_cnt < 4:
        answer = -1
    else:        
        answer = max_cnt
    
    print(f'#{tc} {answer}')