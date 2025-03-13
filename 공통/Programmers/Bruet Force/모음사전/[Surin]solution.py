"""
[모음사전]
- 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는
- 길아 5 이하의 모든 단어 수록
- 몇 번째 단어일까?

- 1 <= len(word) <= 5
"""

def solution(word):
    answer = 0
    
    char_list = ['A', 'E', 'I', 'O', 'U']
    visited = [0] * 5
    
    cnt = 0
    
    # 조합 찾기
    def dfs(subset):
        nonlocal cnt, word, answer
        
        if subset:
            cnt += 1
            if word == ''.join(subset):
                answer = cnt
            
        if sum(visited) == 5:
            return
        
        for i in range(5):
            
            if visited[i] < 6:
                visited[i] += 1
                dfs(subset+[char_list[i]])
                
                if answer != 0:
                    break
                
                visited[i] -= 1
            
    dfs([])
        
    return answer

word = 'AAAAE'

print(solution(word))