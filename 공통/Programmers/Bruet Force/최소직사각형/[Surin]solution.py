def solution(sizes):
    N = len(sizes)
    cards = [[0]*N for _ in range(2)]    # 가로와 세로 중 더 큰 값을 0번 행에 넣어줄 예정
    
    for i, size in enumerate(sizes):
        w, h = size[0], size[1]
        if w > h:
            cards[0][i], cards[1][i] = w, h
        else:
            cards[0][i], cards[1][i] = h, w
    
    max_w, max_h = max(cards[0]), max(cards[1])
    
    answer = max_w * max_h
    
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))