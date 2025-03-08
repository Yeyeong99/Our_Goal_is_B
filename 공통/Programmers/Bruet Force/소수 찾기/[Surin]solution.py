"""
[소수 찾기]
- 한 자리 숫자가 적힌 종이 조각
- 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있을까?
- 각 종이 조각에 적힌 숫자가 적힌 문자열 : numbers
- 종이 조각으로 만들 수 있는 소수는?
"""
def solution(numbers):
    
    # 숫자 리스트로 저장
    number_list = [int(num) for num in numbers]
    
    # 방문 기록 확인용
    visited = [0]*len(number_list)
    
    # 원소 넣는 리스트
    subset = []
    
    # 부분집합들 넣는 리스트
    subset_list = []
    
    # 부분집합 구하는 함수
    def dfs(arr, visited, subset_list):
        nonlocal number_list
        
        if arr:  # 공집합 제외하고
            num = int(''.join(map(str, arr)))
            if num > 1:
                if num not in subset_list:
                    subset_list.append(num)

        for i in range(len(number_list)): 
            
            if not visited[i]:  # 방문하지 않았다면
                
                visited[i] = True    # 방문했고
                arr.append(number_list[i])    # 리스트 넣어주었고
                dfs(arr, visited, subset_list)
                
                # 백트래킹
                arr.pop()  
                visited[i] = False
    
    # 부분집합을 구했다.
    dfs(subset, visited, subset_list)
    
    # 소수 찾는 함수
    def find_prime_number(n):
        nonlocal answer
        
        for i in range(2, n):    # 2부터 n-1까지 중에 나눠지는 것이 있으면 소수가 아니다.
            if n % i == 0:
                break
        else:
            answer += 1
        
    answer = 0
    
    for sub_num in subset_list:
        find_prime_number(sub_num)
    
    return answer

numbers = '011'

print(solution(numbers))