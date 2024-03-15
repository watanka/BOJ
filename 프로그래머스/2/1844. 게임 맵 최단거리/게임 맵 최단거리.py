from collections import deque

def solution(maps):
    
    M, N = len(maps), len(maps[0])
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def bfs(y, x):
        queue = deque([[y, x]])
        
        
        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                
                if 0 > ny or ny >= M or 0 > nx or nx >= N:
                    continue
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((ny, nx))
                    if ny == M-1 and nx == N-1:
                        return 
    bfs(0, 0)
    
    return maps[-1][-1] if maps[-1][-1]!=1 else -1
    
            
            
                    
    