# swea 20551
import sys
sys.stdin = open("txt/2055.txt", "r")

def check(arr):
    ans = 0

    if arr[0] > 0 and arr[1] > 1 and arr[1] > 2:
        ans = 0

    if arr[1] >= arr[2]:     # 두번째 사탕수가 더 작으면
        while arr[1] >= arr[2]:
            arr[1] -= 1
            if arr[1] == 1:
                ans = -1
                break
            ans += 1

    if arr[0] >= arr[1]:     # 두번째 사탕수가 더 작으면
        while arr[0] >= arr[1]:
            arr[0] -= 1
            if arr[0] == 0:
                ans = -1
                break
            ans += 1

    return ans

T = int(input())
for tc in range(1,T+1):

    candy_arr = list(map(int, input().split()))

    answer = check(candy_arr)

    print(f'#{tc} {answer}')