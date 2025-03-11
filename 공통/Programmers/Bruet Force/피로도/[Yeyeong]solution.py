def solution(k, dungeons):
    total_list = []
    def dfs(n, cnt, dungeons, visited):
        nonlocal total_list
        if len(visited) == n:
            print(visited)
            total_list += [visited]
            print(total_list)
        else:
            for d in range(len(dungeons)):
                if dungeons[d] not in visited:
                    visited += [dungeons[d]]
                    dungeons_left = dungeons[:d] + dungeons[d + 1:]
                    cnt += 1
                    dfs(n, cnt, dungeons_left, visited)
                    cnt -= 1
                    dungeons_left = dungeons
                    visited.pop()

    dfs(len(dungeons), 0, dungeons, [])
    print(total_list)
    max_num = -99999999
#     numbers = 0
#     for total in total_list:
#         for i in range(len(dungeons) - 1):
#             left = total[i][0] - total[i][1]
#             if total[i + 1][0] < left:
#                 numbers += 1
#         max_num = max(numbers, max_num)
    
    
    return max_num
