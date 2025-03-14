# 완전 탐색을 사용한다.
# 각 달에 4가지 케이스를 모두 확인하며 진행함.
def recur(month, total):
    global answer

    if month > 12:    # 12월까지 확인하면
        answer = min(answer, total)
        return

    if total > answer:
        return

    # 1일
    recur(month+1, total + day*planner[month])
    # 한달
    recur(month+1, total + month1)
    # 세달
    recur(month+3, total + month3)
    # 일년
    recur(month+12, total + year)


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 이용권 요금 (4개 고정)
    day, month1, month3, year = map(int, input().split())

    # 이용 계획
    planner = [0] + list(map(int, input().split()))

    answer = int(21e8)

    recur(1, 0)

    print(f'#{tc} {answer}')