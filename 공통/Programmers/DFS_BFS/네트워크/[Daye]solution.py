# union-find 문제같음

# 컴퓨터 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어짐

# 여기서 제대로 부모 갱신을 안해줬어서 오류생겼음.. return find_parent(parent, parent[x]) 를 하면 마지막에 answer구할 때 오류생김
# return 을 하면 최상위 루트를 가져오긴하지만.. 결과를 저장하진않음 단순히 루트만 찾는겅미
def find_parent(parent,x):
    if parent[x] != x:
        # 경로 압축 (x의 부모를 최상위 루트로 바꿔줌 )
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    u_a = find_parent(parent,a)
    u_b = find_parent(parent,b)

    if u_a < u_b:
        parent[u_b] = u_a
    else:
        parent[u_a] = u_b

def solution(n, computers):
    # 연결 확인 보기 좋게
    # ex ) connect[0] = [1,2] 다 컴퓨터 0은 컴퓨터 1,2 와 연결.... 보기 쉽게 하려고 리스트 생성
    connect = [[]for _ in range(n)]

    # 같은 네트워크를 이어주기 위한 변수
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            # [1][1]..[n][n] 은 1이라 제외하고 봄.
            if i != j and computers[i][j] ==1:
                connect[i].append(j)

    # 같은 네트워크면 합쳐주는 함수
    for i in range(len(connect)):
        if len(connect[i]) != 0:
            for j in range(len(connect[i])):
                union(parent,i,connect[i][j])

    answer = 0

    for idx in range(n):
        if parent[idx] == idx:
            answer += 1

    return answer

# aa = solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
#
# print(aa)