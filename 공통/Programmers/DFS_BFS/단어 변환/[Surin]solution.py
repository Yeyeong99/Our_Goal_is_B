"""
[단어 변환]
- begin에서 target으로 변환

[조건]
- 한번에 하나씩만 변환
- words에 있는 단어로만 변환가능
- 반환 불가능하면 0
"""

def solution(begin, target, words):
    answer = 0

    # 1. 현재 문자에서 하나만 다른 글자를 찾는다.
    # 2. 1번 반복
    # 3. 끝까지 봤는데 안나오면 0 / 끝까지 보기 전에 해당 글자가 나오면 words의 첫 번째 글자 부터 다시 시작
    
    def dfs(cnt, words, visited, subset):
        if cnt == len(words):
            pass

        for idx, word in enumerate(words):
            pass
    
    return answer