# 프로그래머스 k번째 수

def solution(array, commands):

    answer = []

    # i번째 수부터 j번째 수까지 자르고 정렬한뒤에 자른 숫자 k번째 숫자 구하기 
    for i, j, k in commands:

        cut = array[i-1:j]
        cut.sort()
        answer.append(cut[k-1])

    return answer


# print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))