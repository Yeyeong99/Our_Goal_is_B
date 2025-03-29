# 프로그래머스 단어 변환 문제
# dfs 이용
# 바꿀 수 있는 모든 경우의 수 보는거

answer = 1e9

def dfs(b,t,words,cnt):
    global answer

    # 백트래킹
    if cnt > answer:
        return

    # 현재 단어와 target 단어가 같으면 return
    if b == t:
        if cnt < answer:
            answer = cnt
            return

    # target 이 words 안에 있지않으면 볼 필요없음
    if cnt == 0 and t not in words:
        answer = 0
        return

    for word in words:
        # 같은 알파벳 체크
        check = check_same(b,word)
        if check:
            new_b = word
            words.remove(word)
            dfs(new_b,t,words,cnt + 1)
            words.append(new_b)

# 알파벳 하나만 달라야지 바꿀 수 있음 .
def check_same(a,b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def solution(begin, target, words):
    dfs(begin,target,words,0)
    return answer


# result =solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
#
# print(result)

# 처음에 단어 한글자 다른 걸 set 교집합으로 풀라했음 -> 문제점 : diss 같이 중복된 알파벳이 있는 단어가 있을 수도 있는데 set를 사용하면 이러한 case를 고려하지않아 틀림