N, K = map(int, input().split())
# print(N, K)    # N = len(weather)   # K = 며칠 합해야하는가?
weather = list(map(int, input().split()))
# print(weather)

max_sum = [sum(weather[:K])]

for i in range(N-K):
    max_sum.append(max_sum[i] - weather[i] + weather[i+K])

print(max(max_sum))


''' 시간초과
N, K = map(int, input().split())
# print(N, K)    # N = len(weather)   # K = 며칠 합해야하는가?
weather = list(map(int, input().split()))
# print(weather)

w_sum = 0
max_w_sum = 0
for i in range(N):
    w_sum = sum(weather[i:i+K])
    if max_w_sum < w_sum:
        max_w_sum = w_sum

print(max_w_sum)
'''