# 최적 경로

#import sys
#sys.stdin = open("input.txt", "r")

from itertools import permutations

def distance(arr):
    global short
    d = 0

    d += abs(firm[0] - arr[0][0]) + abs(firm[1] - arr[0][1])

    for i in range(len(customer)-1):
        if d > short :
            return
        d += abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1])

    d += abs(arr[-1][0] - home[0]) + abs(arr[-1][1] - home[1])

    if d < short:
        short = d

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())                        # N 고객의 수
    xy = list(map(int, input().split()))     # 좌표 리스트

    firm = []
    home = []
    customer = []

    short = 1e9

    # 회사 좌표 / 집 좌표 추가
    firm.extend([xy[0], xy[1]])
    home.extend([xy[2], xy[3]])

    # 고객좌표 리스트 추가
    for idx in range(4, len(xy), 2):
        customer.append([xy[idx], xy[idx+1]])

    # 순열로 모든 경로 경우의 수 구함
    for order in permutations(customer):
        distance(order)


    print(f"#{test_case} {short}")

    # ///////////////////////////////////////////////////////////////////////////////////
