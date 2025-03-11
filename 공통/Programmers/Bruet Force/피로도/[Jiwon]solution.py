# 완전탐색
import itertools

def solution(k, dungeons):
    dungeon_list = list(itertools.permutations(dungeons))
    max_count = 0


    for i in range(len(dungeon_list)):
        count = 0
        current_fatigue = k
        for j in range(len(dungeon_list[i])):
            min_fatigue, consume_fatigue = dungeon_list[i][j]
            if current_fatigue >= min_fatigue:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                break
            current_fatigue = current_fatigue - consume_fatigue

    return max_count

# DFS BFS로도 풀어보기