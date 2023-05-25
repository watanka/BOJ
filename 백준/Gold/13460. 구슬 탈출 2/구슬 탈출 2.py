## 구슬 탈출 2
from collections import deque

N, M = map(int, input().split())                                                           
board = [list(input().strip()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = [-1,0,1,0], [0,1,0,-1]
q = deque()

for j in range(N) :
    for i in range(M) :
        if board[j][i] == 'R' :
            ry, rx = j, i
        elif board[j][i] == 'B' :
            by, bx = j, i
q.append((ry, rx, by, bx, 1))
visited[ry][rx][by][bx] = True

def move(y, x, dy, dx) :
    cnt = 0
    while board[y+dy][x + dx] != '#' and board[y][x] != 'O' :
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs() :
    while q :
        ry, rx, by, bx, depth = q.popleft()
        if depth > 10 :
            break
        for i in range(len(dx)) :
            next_ry, next_rx, r_cnt = move(ry, rx, dy[i], dx[i])
            next_by, next_bx, b_cnt = move(by, bx, dy[i], dx[i])

            if board[next_by][next_bx] == 'O' :
                continue
            if board[next_ry][next_rx] == 'O' :
                print(depth)
                return

            if next_ry == next_by and next_rx == next_bx :
                if r_cnt > b_cnt :
                    next_ry -= dy[i]
                    next_rx -= dx[i]
                else :
                    next_by -= dy[i]
                    next_bx -= dx[i]
                
            if not visited[next_ry][next_rx][next_by][next_bx] :
                visited[next_ry][next_rx][next_by][next_bx] = True
                q.append((next_ry, next_rx, next_by, next_bx, depth + 1))
    print(-1)

bfs()