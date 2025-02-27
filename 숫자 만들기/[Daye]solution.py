
def dfs(idx, operator, calculation):

    if idx == N:                                                           # idx 가 주어진 숫자의 개수와 같아지면 인덱스는 숫자 개수보다 -1 이므로 
        result.append(calculation)                                         # 주어진 숫자를 다 이용했다는 것을 알 수 있으므로 계산이 끝난 걸 암 
        return                                                          
    
    if operator[0] >= 1:                                                   # operator[0] 은 +
        operator[0] -= 1                                                   # + 를 썼으니까 횟수 차감 
        dfs(idx+1, operator, calculation + numbers[idx])
        operator[0] += 1                                                   # 다시 더해야하는게 다음 if 문에서 줄인 값 들어가면 결과 이상하게 됨 

    if operator[1] >= 1:                                                   # operator[1] 은 - 
        operator[1] -= 1
        dfs(idx+1, operator, calculation - numbers[idx])
        operator[1] += 1

    if operator[2] >= 1:                                                   # operator[2] 는 *
        operator[2] -= 1
        dfs(idx+1, operator, calculation * numbers[idx])
        operator[2] += 1
    
    if operator[3] >= 1:                                                   # operator[3] 는 /
        operator[3] -= 1
        dfs(idx+1, operator, int(calculation / numbers[idx]))
        operator[3] += 1




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    # N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했다.
    # 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.
    # 예를 들어 1, 2, 3 이 적힌 게임 판에 +와 x를 넣어 1 + 2 * 3을 만들면 1 + 2를 먼저 계산하고 그 뒤에 * 를 계산한다.
    # 즉 1+2*3의 결과는 9이다.
    # 주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오

    # 아이디어 : dfs 를 이용해 연산자 순위를 고려한 모든 경우의 수를 구해봄.

    N = int(input())                                                   # N개의 숫자
    operator_num = list(map(int,input().split()))                      # 연산자 갯수 + = * /        ex) 2 1 0 1 (+ 2개 , - 1개 , * 0개 , / 1개)
    numbers = list(map(int,input().split()))                           # 사용하는 숫자들

    result = []                                                        # 모든 경우의 수 결과값을 담아줄 리스트 

    dfs(1, operator_num, numbers[0])

    difference = max(result)- min(result)   

    print(f"#{test_case} {difference} ")
    # ///////////////////////////////////////////////////////////////////////////////////
