def solution(citations):

    answer=0

    for num in range(1,len(citations)+1):
        check = 0
        for i in citations:
            if num<=i:
                check += 1
        if check >= num:
            answer = num

    return answer

# print(solution([3, 0, 6, 1, 5]))