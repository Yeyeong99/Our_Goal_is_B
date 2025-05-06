# 백준 14888 (연산자 끼워넣기)

# 수열 , 연산자 주어짐 이들을 조합해서 계산된 결과의 최댓값 , 최소값 구하기

def calculate(arr):

    global max_sum, min_sum

    # 연산자 순서대로 앞에서부터 계산
    temp = arr[:]  # 얕은 복사로 원본 유지
    result = temp[0]
    for i in range(1, len(temp), 2):
        operator = temp[i]
        number = temp[i+1]

        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        elif operator == '/':
            if result < 0:
                result = -(-result // number)
            else:
                result = result // number

    max_sum = max(max_sum, result)
    min_sum = min(min_sum, result)

def dfs(idx,op,cal):

    if idx == N:
        calculate(cal)
        return

    for i in range(len(op)):
        if op[i] > 0:
            cal.append(operators[i])
            cal.append(numbers[idx])
            op[i] -= 1
            dfs(idx + 1, op, cal)
            op[i] += 1
            cal.pop()  
            cal.pop()  


# N 수의 개수
N = int(input())

# 숫자들 
numbers = list(map(int,input().split()))

# 연산자 개수 ( + , -, *, / )  -> 개수 합하면 N-1개
operator_num = list(map(int,input().split()))
operators = ['+', '-', '*', '/']

min_sum =  int(1e9)
max_sum = -int(1e9)

# 숫자 idx, 연산자 개수, 식 담을 리스트 
# dfs(0,operator_num,[])
dfs(1, operator_num, [numbers[0]])

print(max_sum)
print(min_sum)
