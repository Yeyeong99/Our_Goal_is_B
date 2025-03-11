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
    visited = [0]*5
    
    cnt = 0
    
    def dfs(i, subset_list):
        nonlocal cnt, answer
        
        if i == 5:
            return
        
        if sum(visited) == 5:
            return
        
        if subset_list:
            cnt += 1
            target = ''.join(subset_list)
            print(target)
            if target == word:
                answer = cnt
        
        visited[i] += 1
        dfs(0, subset_list+[char_list[i]])
        
        visited[i] -= 1
        dfs(i+1, subset_list)
        
    dfs(0, [])
        
    return answer

word = 'AAAAE'

print(solution(word))