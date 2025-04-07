"""
n 편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다.
"""


def solution(citations):
    answer = 0

    n = len(citations)
    # 인용횟수 정렬하기
    citations.sort()    # 오름차순

    for h in range(1, n+1):
        for i, citation in enumerate(citations, 1):
            if citation >= h:    # 인용횟수가 h보다 크거나 같다면
                h_max = n-i+1    # h번 이상 인용된 논문의 수
                if h_max >= h:    # 인용된 논문이 h편 이상이고
                    answer = max(answer, h)

    return answer

citations = [3, 0, 6, 1, 5]

print(solution(citations))
