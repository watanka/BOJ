## 알고스팟
from collections import deque

M, N = map(int, input().split())

maze = []
for _ in range(N) :
    maze.append(list(map(int, list(input()))))

moves = [(1,0), (0,1), (-1, 0), (0,-1)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

def bfs() :
    queue = deque([(0,0)])
    dist[0][0] = 0

    while queue :
        y, x = queue.popleft()
        
        for dy, dx in moves :
            ny, nx = y + dy, x + dx
            if (0 <= ny < N) and (0 <= nx < M) :
                if dist[ny][nx] == -1 :
                    if maze[ny][nx] == 0 :
                        dist[ny][nx] = dist[y][x]
                        queue.appendleft((ny, nx))
                    else :
                        dist[ny][nx] = dist[y][x] + 1
                        queue.append((ny, nx))
                if ny == M-1 and nx == N-1 :
                    return  

bfs()

print(dist[N-1][M-1])