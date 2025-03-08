## dfs 버전

def synergy(arr):
    food_synergy = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            food_synergy += food[arr[i]][arr[j]] + food[arr[j]][arr[i]]
    return food_synergy

def dfs(k, i):
    global minimum

    if k == N//2 :          # 음식 재료 N//2 선택했으면 시너지계산 나머지 N//2는 알아서 따라옴
        food_a = []
        food_b = []
        for i in range(N):
            if visited[i] == 1:
                food_a.append(i)
            else:
                food_b.append(i)

        a = synergy(food_a)
        b = synergy(food_b)
        minimum = min(minimum, abs(a-b))
        return

    for idx in range(i,N):
        if not visited[idx]:
            visited[idx] = 1
            dfs(k+1, idx+1)
            visited[idx] = 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())                    # 식재료 개수

    food = [list(map(int,input().split())) for _ in range(N)]             # 음식 시너지
    visited = [0] * N       # visited 를 이용해 음식 재료 짝 지어줌 .

    minimum = 999999

    dfs(0, 0)       # 음식 재료 선택 수 / 인덱스 전달

    print(f"#{test_case} {minimum}")
    # ///////////////////////////////////////////////////////////////////////////////////




