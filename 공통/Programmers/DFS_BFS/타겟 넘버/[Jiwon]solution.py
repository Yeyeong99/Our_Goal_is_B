from itertools import product

def calc_(nums, operators):
    result = nums[0]
    for j in range(1, len(nums)):
        if operators[j-1] == '+':
            result += nums[j]
        elif operators[j-1] == '-':
            result -= nums[j]
    return result

def solution(numbers, target):
    numbers.insert(0, 0)  # 앞에 0을 넣어줘서 연산이되도록 한다.. 0을 안넣고 할수는 없을까 생각 해보기.
    global k
    count = 0
    for i in product(k, repeat=len(numbers)-1):
        op_list = i
        result = calc_(numbers, op_list)
        if result == target:
            count += 1
    return count

k = ['+', '-']


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
