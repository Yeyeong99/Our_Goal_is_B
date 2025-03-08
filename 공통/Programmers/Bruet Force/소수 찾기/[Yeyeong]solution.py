from itertools import permutations
def solution(numbers):
    perms = []
    for n in range(len(numbers) + 1):  # 숫자를 만들 수 있는 모든 경우의 수
        perms += list(permutations(numbers, n)) 
    perms = list(set(perms))  # 중복된 경우 없애줌

    answer = 0
      
    for perm in perms:
        if perm and perm[0] != '0':  # 공집합일 때, 0으로 시작되는 경우 없애기
            current = int(''.join(perm))
            prime_num = []
            for num in range(1, current + 1):
                if current % num == 0:
                    prime_num.append(num)
                if len(prime_num) >= 3:
                    break
            if prime_num == [1, current]:
                answer += 1
    
    return answer
