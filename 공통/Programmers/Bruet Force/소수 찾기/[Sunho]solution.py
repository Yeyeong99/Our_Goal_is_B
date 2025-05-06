from itertools import permutations

def solution(numbers):
    answer = 0

    n = len(numbers)

    subset = set()
    for i in range(1, n+1):
        subset.update(permutations(numbers, i))
        subset_list = list(map(list, subset))
    # print(subset_list)
    m = len(subset_list)
    num_list = []

    for i in range(m):
        # print(int("".join(subset_list[i])))
        num_list.append(int("".join(subset_list[i])))\
    # print(num_list)

    for x in set(num_list):
        if x > 1:
            n = 2
            while n < x:
                if x % n == 0:
                    break
                if n == x-1:
                    answer += 1
                    # print(x)
                    break
                n += 1

    return answer


numbers = list(input())   #  길이 1 이상 7 이하인 문자열(0~9까지 숫자만으로 이루어짐)
ans = solution(numbers)

print(ans)