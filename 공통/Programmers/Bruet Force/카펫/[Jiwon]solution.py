def solution(brown, yellow):
    carpet = brown + yellow
    yaksu = []
    for i in range(1, carpet + 1):
        if carpet % i == 0:
            j = carpet // i
            yaksu.append([i, j])

    yaksu = yaksu[(len(yaksu))//2:]

    for item in yaksu:
        if 2 * item[0] + 2 * item[1] - 4 == brown:
            return item

# solution(10, 2)
# solution(8, 1)
# solution(24, 24)