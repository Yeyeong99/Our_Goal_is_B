"""
[단어 변환]
- begin에서 target으로 변환

[조건]
- 한번에 하나씩만 변환
- words에 있는 단어로만 변환가능
- 반환 불가능하면 0
"""

def solution(begin, target, words):
    # 모든 단어의 길이
    N = len(target)

    answer = len(words)+1
    visited = [False]*len(words)

    # 1. 현재 문자에서 하나만 다른 글자를 찾는다.
    # 2. 1번 반복
    # 3. 끝까지 봤는데 안나오면 0 / 끝까지 보기 전에 해당 글자가 나오면 words의 첫 번째 글자 부터 다시 시작

    def dfs(start, subset):
        nonlocal answer

        # subset의 길이가 더 길면 더 많이 거쳤다는 말
        if len(subset) >= answer:
            return

        # target을 만나면
        if start == target:
            answer = min(len(subset), answer)
            return

        # if cnt == N:
        #     return

        for i in range(len(words)):    # 주어진 단어 길이만큼 돈다.
            if not visited[i]:  # 방문한 적이 없다면
                # 현재 문자에서 하나만 다른 글자 찾기
                diff = 0
                for c in range(N):
                    if start[c] != words[i][c]:
                        diff += 1

                if diff == 1:    # 하나만 다르다!
                    visited[i] = True
                    dfs(words[i], subset+[words[i]])
                    visited[i] = False

    dfs(begin, [])

    if answer == len(words)+1:
        return 0

    if answer != 0:
        return answer

    return answer