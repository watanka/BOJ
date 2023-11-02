from collections import deque
def solution(maps):
    answer = 10001
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    n, m = len(maps), len(maps[0])
    
    def bfs(pos) :
        queue = deque([pos])
        while queue :
            cur_y, cur_x = queue.popleft()
            for dy, dx in directions :
                new_y, new_x = cur_y + dy, cur_x + dx
                if 0 <= new_y < n and 0 <= new_x < m and maps[new_y][new_x] == 1 :
                    maps[new_y][new_x] = maps[cur_y][cur_x] + 1
                    queue.append((new_y, new_x))
        return maps[-1][-1]
    
    answer = bfs((0,0))

    return answer if answer != 1 else -1
        
                    
    