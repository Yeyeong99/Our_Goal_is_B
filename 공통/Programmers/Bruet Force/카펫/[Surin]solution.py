def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:    # 인수이면
            if (n // i) < i:    # 몫이 나누는 수보다 크면
                break    # 끝낸다.
            else:
                factors.append([i, n//i])
    
    return factors


def solution(brown, yellow):
    answer = []
    
    # 노란색 부분의 인수들 확인하기
    yellow_factors = find_factors(yellow)
    
    # 갈색 부분 = 노란색 부분의 인수 쌍 * 2 + 4
    for factor in yellow_factors:
        w, h = factor[0], factor[1]
        if (w + h) * 2 + 4 == brown:
            w += 2
            h += 2
            break
    
    if w >= h: 
        answer = [w, h]
    else:
        answer = [h, w]
    
    return answer