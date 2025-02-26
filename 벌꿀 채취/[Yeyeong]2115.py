import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]

    stack = []
    for i in range(N):
        for j in range(N - M + 1):
            current_honey = []
            for k in range(M):
                current_honey.append(honeys[i][j + k])
            if not stack:
                stack.append(current_honey)
            else:
                last_in = stack[-1]
                if sum(last_in) <= sum(current_honey):
                    stack.pop()
                    stack.append(current_honey)
    print(stack)
