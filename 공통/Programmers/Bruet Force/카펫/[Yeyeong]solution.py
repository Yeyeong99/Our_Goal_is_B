def solution(brown, yellow):
    total = brown + yellow
    nums = [i for i in range(total + 1, 0, -1) if total % i == 0]
    for w in nums:
        h = total // w
        if (h - 2) * (w - 2) == yellow:
            return w, h
