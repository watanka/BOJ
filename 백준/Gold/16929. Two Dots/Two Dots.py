## Two Dots

N, M = map(int, input().split())

board = []
for _ in range(N) :
    board.append(list(input()))

moves = [[0,1], [0,-1], [1,0], [-1,0]]

ans = False

def dfs(letter, y, x, cnt, start_y, start_x) :
    global ans
    if ans :
        return

    for (dy, dx) in moves :
        ny = y + dy
        nx = x + dx
        if (0 <= ny < N) and (0 <= nx < M) :
            
            if cnt >= 4 and (nx == start_x and ny == start_y) :
                ans = True
                return
            
            if not visited[ny][nx] and board[ny][nx] == letter :
                visited[ny][nx] = 1
                dfs(letter, ny, nx, cnt + 1, start_y, start_x)
                visited[ny][nx] = 0





found = False
visited = [[0 for _ in range(M)] for _ in range(N)]

for j in range(N) :
    for i in range(M) :
        visited[j][i] = 1
        dfs(board[j][i], j, i, 1, j, i )

        if ans :
            print('Yes')
            found = True
            break
    if found :
        break
if not found :
    print('No')