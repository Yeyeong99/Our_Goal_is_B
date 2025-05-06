def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # 정렬해야 할 배열
        array_to_sort = array[i-1:j]
        # 정렬하고
        for p in range(len(array_to_sort)-1):
            for q in range(p, len(array_to_sort)):
                if array_to_sort[p] > array_to_sort[q]:
                    array_to_sort[p], array_to_sort[q] = array_to_sort[q], array_to_sort[p]
        # 숫자 고르기
        answer.append(array_to_sort[k-1])
                    
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
