T = int(input())
for t in range(T):
    n, m = map(int, input().split())

    diff = m - n + 1
    num = 1
    result = 0

    while diff > 0:
        result += diff * num
        diff -= 1
        num += 1

    print(result)