def solution(k, dungeons):
    min_list = []
    def dfs(n, cnt, dungeons, visited):
        nonlocal min_list
        if len(visited) == n:
            min_list.append(cnt)
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
    
    return max(min_list)
