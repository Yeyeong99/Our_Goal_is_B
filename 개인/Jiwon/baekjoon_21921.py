N, X = map(int, input().split())
visitors = list(map(int, input().split()))

# 1일부터 x일까지 합을 계산함  x_sum
# x_sum -1 + x+1
# x_sum -2 + x+2
# x_sum -3 + x+3 ... 해주면됨

# 슬라이딩 윈도우 알고리즘.

current_sum = sum(visitors[:X])
max_visitors = current_sum
count = 1        # 첫번째 윈도우 이미 만들엇으ㅁ니까 카운트 1부터임
for i in range(1, N - X + 1):
    current_sum = current_sum - visitors[i - 1] + visitors[i + X - 1]
    if current_sum > max_visitors:
        max_visitors = current_sum
        count = 1
    elif current_sum == max_visitors:
        count += 1
if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(count)
