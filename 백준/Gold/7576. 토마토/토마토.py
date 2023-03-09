## 토마토
from collections import deque
M, N = map(int, input().split())

box = []
for _ in range(N) :
    box.append(list(map(int, list(input().split()))))

visited = [[0 if box[j][i] != -1 else -1 for i in range(M)] for j in range(N)]


moves = [[0,1], [0,-1], [1,0], [-1,0]]

tomatoes = deque()
for j in range(N) :
    for i in range(M) :
        if box[j][i] == 1 :
            visited[j][i] = 1
            tomatoes.append([j,i])

while tomatoes :
    y,x = tomatoes.popleft()
    for mv in moves :
        dy, dx = mv
        if (0 <= y + dy < N) and (0 <= x + dx < M) : 
            ny, nx = y + dy, x + dx
            if box[ny][nx] == 0 and visited[ny][nx] == 0 :
                visited[ny][nx] = visited[y][x] + 1
                tomatoes.append((ny, nx))

result = -1
over = False
for row in visited :
    for i in row :
        if i == 0 :
            print(-1)
            over = True
            break
        result = max(result, i)
    if over :
        break
if not over :
    print(result - 1)