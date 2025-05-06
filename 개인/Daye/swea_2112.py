# 깊은복사 deepcopy는 시간 많이 잡아먹음 . 슬라이스 복사가 훨 빠름

# 필름 두께 D, 가로 크기 W의 보호 필름


import sys
sys.stdin = open("sample_input.txt", "r")

# 약품 투입
def drug(depth, cnt, film):
    global result

    if cnt >= result:
        return
    
    if depth == D:
        if inspect(film):  # True/False만 반환하도록
            result = cnt
        return

    # 1. 안 바꾸고 다음 줄로
    drug(depth+1, cnt, film)

    # 2. A(0)로 바꾸고 다음 줄로
    temp = [row[:] for row in film]
    temp[depth] = [0] * W
    drug(depth+1, cnt+1, temp)

    # 3. B(1)로 바꾸고 다음 줄로
    temp = [row[:] for row in film]
    temp[depth] = [1] * W
    drug(depth+1, cnt+1, temp)

# 성능 검사
def inspect(arr):
    global result

    test = 0

    for j in range(W):
        charac = 1
        for i in range(1,D):
            if arr[i][j] == arr[i-1][j]:
                charac += 1
            else :
                charac = 1
            if charac == K :
                test += 1
                break

    if test == W:
        return True
    else:
        return False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # D 필름 세로 / W 가로 / K = 합격 기준
    D, W, K= map(int,input().split())

    film = [list(map(int,input().split())) for _ in range(D)]

    result = 15

    drug(0,0,film)

    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
