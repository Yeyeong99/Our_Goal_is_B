import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(math.comb(M, N))  # M개 중 N개를 선택하는 조합 계산
