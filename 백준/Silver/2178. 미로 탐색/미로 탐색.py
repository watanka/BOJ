## 미로 탐색
N, M = map(int, input().split())

maze = []
for _ in range(N) :
    maze.append(list(map(int, list(input()))))


visited = [[0 for _ in range(M)] for _ in range(N)]
moves = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(y,x) :
    queue = [(y,x)]
    visited[y][x] = 1

    while queue :
        qy, qx = queue.pop(0)
        if qy == N-1 and qx == M-1 :
            return visited[qy][qx]

        for mv in moves :
            h,w = mv
            ny, nx = qy + h, qx + w
            if (0 <= ny < N) and (0 <= nx < M) :
                if not visited[ny][nx] and maze[ny][nx] :
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[qy][qx] + 1
                

print(bfs(0,0))

