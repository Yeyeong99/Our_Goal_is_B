def solution(begin, target, words):
    from collections import deque
    used = [0] * len(words)
    
    def find_word(b, t, w):
        nonlocal used
        
        difference = 0
        for i in range(len(b)):
            if b[i] != t[i]:
                difference += 1
        if difference == 1:
            return t
        same = 0
        
        for i in range(len(w)):
            for j in range(len(begin)):
                if not used[i] and b[j] == w[i][j]:
                    same += 1
            if same == 2:
                used[i] = 1
                return w[i]
            
    def bfs(begin, target, count):
        if target not in words:
            return 0
        
        queue = deque()
        queue.append((begin, target, count))
        
        while queue:
            b, t, cnt = queue.popleft()
            new_word = find_word(b, t, words)
            
            if new_word == t:
                return cnt + 1
            
            queue.append((new_word, t, cnt + 1))
                            
    answer = bfs(begin, target, 0)
    return answer
