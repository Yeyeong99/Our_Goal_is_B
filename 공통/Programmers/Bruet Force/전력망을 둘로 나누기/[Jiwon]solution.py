def solution(n, wires):
    # bfs??

    graph = [[] for _ in range(n+1)]
    answer = -1
    return answer


# n 송전탑의 개수 # wires 전선정보
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))