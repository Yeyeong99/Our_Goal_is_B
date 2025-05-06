from itertools import product
# 가능한 모든 조합
# 데카르트 곱..
# 여러 개의 리스트에서 하나씩 선택하여 나올 수 있는 "모든 경우의 수(중복 포함)"생성


def solution(word):
    dictionary = []    # 가능한단어 저장
    for length in range(1, 6):  # 단어길이 1~5글자
        for item in product("AEIOU", repeat=length):
            # 문자열 AEIOU 에서 length 길이만큼 문자를 뽑아서 만들 수 있는 모든 경우의 수 반환
            # length = 3이면 길이 3인 모든 단어 생성..
            # for length in range(1, 6) 이라고 했으므로 length = 1, 2, 3, 4, 5인 단어를 전부 생성.
            dictionary.append("".join(item))   # 튜플로 반환되므로 join 해준다.

    dictionary.sort()
    position = 1
    for w in dictionary:
        if w == word:
            return position
        position += 1


