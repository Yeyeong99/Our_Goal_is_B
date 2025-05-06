# https://school.programmers.co.kr/learn/courses/30/lessons/42839
import itertools

def is_prime_num(num):  # 소수 판별
    if num < 2:
        return False  # 0,1 소수아님

    if num == 2:
        return True  # 2 소수임

    for i in range(2, num):  # 1과 num을 제외한 사이의 수로 나눴을때
        if num % i == 0:  # 0으로 떨어지는게 있으면 소수 아님
            return False
            # 없으면 소수.
    return True

def solution(numbers):  # 입력가지고 조합만들기
    num_set = set()  # set으로 중복제거 (07, 7은 같은수임)
    for i in range(1, len(numbers) + 1):
        for p in itertools.permutations(numbers, i):  # i자리 조합을 다만들고
            num = int(''.join(p))  # int로.
            num_set.add(num)

    prime_count = 0
    for num in num_set:
        if is_prime_num(num) == True:
            prime_count += 1
    return prime_count