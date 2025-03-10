
# yellow 넓이 는 (가로 -2 ) * (세로 -2) 이다
def solution(brown, yellow):

    total = brown + yellow

    w_h = []
    answer = []

    # 가로 * 세로 = 전체넓이가 되는 모든 숫자 조합을 찾음
    # 약수는 수/2 한것보다 클 수없기에 total//2 +1 까지 보면됨
    for i in range(1, total//2 + 1):
        if total % i == 0:
            w_h.append([i,total//i])

    # 후보들을 돌면서 조건 충족 하는 후보 찾음
    for r, c in w_h:
        if r >= c and r * c == total and (r-2) * (c-2) == yellow:
            answer.append([r,c])

    return answer[0]

solution(10,2)
