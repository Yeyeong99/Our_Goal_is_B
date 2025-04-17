# 창용 마을 N명의 사람 거주중
# 사람마다 번호가 있음 1 ~ N
# 두 사람이 서로 아는 관계 거나 몇 사람을 거쳐서 알 수 있는 관계라면 하나의 무리
# 이러한 사람들을 모두 다 묶어서 하나의 무리라함 
# 몇개의 무리가 있는지
# Union find 로 접근 

# swea 창용 마을 무리의 개수 
# 풀었움 

T = int(input())

# 특정 원소가 속한 집합을 찾기 
def find_parent(parent,x):
    if parent[x] != x:
        # 경로 압축 (최적화화)
        # return find_parent(parent, parent[x]) 하면 데이터 많을 때 오래걸릴수도
        parent[x] = find_parent(parent, parent[x])
    return x

def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

for tc in range(1,T+1):

    # N 마을 사람 수 / M 관계 갯수
    N, M = map(int,input().split())
    
    # 부모 테이블 생성 
    parent = [0] * (N + 1)
    
    # 부모를 자기 자신으로 초기화
    for i in range(1,N+1):
        parent[i] = i

    for _ in range(M):
        a, b = map(int,input().split())
        union_find(parent,a,b)

    result = 0
    for i in range(1, len(parent)):
        if parent[i] == i:
            result += 1

    # gpt가 위 부모테이블 무리 갯수 세는거 고쳐줌 밑 방식으로 권장한다고함 
    # 부모 테이블을 정리해줘야 정확한 루트 기준으로 무리 수 셀 수 있음
    # for i in range(1, N + 1):
    #     parent[i] = find_parent(parent, i)

    # # 이제 루트만 남기고 중복 제거
    # result = len(set(parent[1:]))

    print(f"#{tc} {result}")