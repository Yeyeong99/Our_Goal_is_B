from itertools import combinations

def combinations_(n, m, bad_):
    bad_list = []
    for pair in bad_:
        bad_list.append(sorted(pair))

    count = 0
    for comb in combinations(range(1, n + 1), 3):
        if [comb[0], comb[1]] not in bad_list and [comb[0], comb[2]] not in bad_list and [comb[1], comb[2]] not in bad_list:
            count += 1
    # 1부터 n까지 숫자중에 3개씩 조합
    return count

n, m = map(int, input().split())
bad_ = [list(map(int, input().split())) for _ in range(m)]
print(combinations_(n, m, bad_))


# 시간초과... 다시풀기
# dfs?