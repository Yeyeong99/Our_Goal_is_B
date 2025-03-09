# 프로그래머스 소수찾기 문제

# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 접근 방법
# 1. 적힌 숫자로 나올 수 있는 모든 숫자 부분집합 찾음 ( itertools 로 부분집합만들어줌)
# 2. 나온 숫자가 소수인지 확인

from itertools import permutations

# 소수 인지 체크하는 함수
def check(number):
    global decimal
    #number 문자로 들어와서 정수로 형변환해줌
    number = int(number)
    # 소수는 약수가 1 , 자기자신인 숫자
    if number < 2:
        return
    # number 전에 나눠지는 숫자가 있으면 소수가 아님
    for i in range(2,number):
        if number % i == 0:
            return
    # for 문에 걸리지않았으면 소수
    decimal.append(number)
    return

# 부분집합을 만들고 소수 체크
def subset(arr):
    for length in range(1,len(arr)+1):
        per = list(permutations(arr,length))
        # permutation은 튜플로 결과가 나오기에 join을 통해 합쳐줌
        for p in per:
            check("".join(p))

paper = input()                   # 종이 조각에 적힌 숫자들
numbers =[]                       # 숫자 분리
decimal = []                      # 소수 담을 리스트

# 입력받은 숫자 분리해줌
for i in range(len(paper)):
    numbers.append(paper[i])

subset(numbers)

# 중복되는 조합이 나올 수 있으므로 set 사용
decimal = set(decimal)

print(len(decimal))


# permutation 결과는 항상 튜플로 나온다
# 단일 요소 튜플은 만들 때 반드시 쉼표를 포함해야 한다. 아니면 문자열이나 숫자로 인식
# 결과값은 나오는데 효율 안좋아서 fail 나오느는듯..
