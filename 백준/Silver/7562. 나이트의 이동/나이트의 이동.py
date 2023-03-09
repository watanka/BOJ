## 나이트의 이동
from collections import deque
T = int(input())

knight_moves = [[1,2], [2,1], [-1,-2], [-2,-1], [-1,2], [-2,1], [1,-2], [2,-1]]

def bfs(start, end) :
    sy, sx = start
    ey, ex = end

    queue = deque([start])
    visited[sy][sx] = 1
    while queue :
        y, x = queue.popleft()
        
        for (dy, dx) in knight_moves :
            ny = y + dy
            nx = x + dx
            if (0<= ny < I) and (0<= nx < I) :
                if not visited[ny][nx] :
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny,nx))
                if ny == ey and nx == ex :
                    return



for _ in range(T) :
    I = int(input())
    visited = [[0 for _ in range(I)] for _ in range(I)]
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    
    bfs((sy,sx), (ey, ex))
    print(visited[ey][ex] - 1)

