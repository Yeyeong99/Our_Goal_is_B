import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    operators_num = list(map(int, input().split()))
    numbers = list(input().split())

    operators = ''
    operators_basic = ['+', '-', '*', '/']
    for n in range(4):
        operators += operators_basic[n] * operators_num[n]

    operators_list = list(operators)
    perm = list((map(list, list(set(permutations(operators_list, len(operators_list)))))))
    equations = [numbers[::-1] + p for p in perm]

    result_max = -float('inf')
    result_min = float('inf')
    for equation in equations:
        stack = []
        for e in equation:
            if e.isdecimal():
                stack.append(int(e))
            else:
                fst = stack.pop()
                snd = stack.pop()
                if e == '+':
                    stack.append(fst + snd)
                elif e == '-':
                    stack.append(fst - snd)
                elif e == '*':
                    stack.append(fst * snd)
                elif e == '/':
                    stack.append(int(fst / snd))
        result_max = max(result_max, sum(stack))
        result_min = min(result_min, sum(stack))
    print(f"#{t} {result_max - result_min}")






