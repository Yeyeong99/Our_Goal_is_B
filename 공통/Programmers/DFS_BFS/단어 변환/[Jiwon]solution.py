# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque
def diff(word1, word2):
    # word1과 word2가 한글자만 다른지 비교한다.
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    # 다를때마다 카운트증가해서, 카운트가 1이면 한글자만 다른것.
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        queue = deque([(begin, 0)])
        count = 0
        visited = [False] * len(words)

        while queue:
            current_word, count = queue.popleft()
            if current_word == target:
                return count
            for i in range(len(words)):
                if not visited[i] and diff(current_word, words[i]):
                    visited[i] = True
                    queue.append((words[i], count+1))

        return count

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))