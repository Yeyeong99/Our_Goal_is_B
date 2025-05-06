
total_case = []

def zero_one(arr, n):
    global total_case

    if len(arr) == n:
        total_case.append(arr[:])
        return

    for num in range(2):
        arr.append(num)
        zero_one(arr, n)
        arr.pop()

def solution(numbers, target):
    zero_one([], len(numbers))
    answer = 0

    for case in total_case:
        num_sum = 0
        for idx in range(len(numbers)):
            if case[idx] == 1:
                num_sum += -numbers[idx]
            elif case[idx] == 0:
                num_sum += numbers[idx]
        if num_sum == target:
            answer += 1

    return answer

