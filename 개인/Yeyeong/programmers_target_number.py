def solution(numbers, target):
    def dfs(i, total):
        nonlocal counts
        if i == len(numbers):
            if total == target:
                counts += 1 
            return 

        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])
        
    counts = 0

    dfs(0, 0)
    
    return counts

