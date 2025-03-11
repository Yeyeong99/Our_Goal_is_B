"""
[전력망을 둘로 나누기]
n개의 송전탑 - 하나의 트리 형태
전력망 네트워크를 2개로 분할
두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게
"""

def solution(n, wires):
    answer = -1
    adjust_list = [[0] for _ in range(n+1)]    # 인접리스트
    for v1, v2 in wires:
        adjust_list[v1].append(v2)

    cnt = 0

    # 탐색 >> 요소를 하나씩 건너뛴다면.?
    def dfs(n):

        if not adjust_list[n]:

            return

        pass

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]