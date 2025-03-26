from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    used = [False] * len(words)
    
    def is_one_letter_diff(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff == 1

    def bfs(begin, target):
        queue = deque([(begin, 0)])  # (current word, step count)
        while queue:
            current_word, steps = queue.popleft()
            
            if current_word == target:
                return steps
            
            for i, word in enumerate(words):
                if not used[i] and is_one_letter_diff(current_word, word):
                    used[i] = True
                    queue.append((word, steps + 1))
        
        return 0  # If no transformation sequence exists
    
    return bfs(begin, target)
