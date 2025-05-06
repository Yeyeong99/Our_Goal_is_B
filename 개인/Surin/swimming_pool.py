# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 이용권 요금 (4개 고정)
    day, month1, month3, year = map(int, input().split())

    # 이용 계획
    plans = [0] + list(map(int, input().split()))

    dp = [0] * 13

    # 시작점 초기화 (1, 2월) ==> 3달, 일년은 계산해주지 않는다.
    dp[1] = min(plans[1]*day, month1)
    dp[2] = dp[1] + min(plans[2]*day, month1)

    # 3월부터는 반복하면서 계산해야 함.
    for month in range(3, 13):
        # N월의 최소 비용 후보
        dp[month] = min(dp[month - 3] + month3,    # 1) N-3월에 3개월 이용권을 구입한 경우
                        dp[month - 1] + month1,    # 2) N-1월의 최소 비용 + 한달권 구매
                        dp[month - 1] + day*plans[month])    # 3) N-1월의 최소 비용 + 1일권 구매

    # 12월의 누적 최소 금액, 1년권 비교
    answer = min(dp[12], year)

    print(f'#{tc} {answer}')