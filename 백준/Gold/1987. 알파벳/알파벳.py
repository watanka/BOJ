## 알파벳

row, col = map(int, input().split())

maps = [list(map(lambda x : ord(x) - 65, input().rstrip())) for _ in range(row)]
visited = [0 for _ in range(26)] # 알파벳
visited[maps[0][0]] = 1

directions = [[0,1], [0,-1], [-1,0], [1,0]]

max_step = 1
def dfs(pos, depth) :
    global max_step
    max_step = max(max_step, depth)
    y, x = pos
    
    for dy, dx in directions :
        ny = y + dy
        nx = x + dx

        if 0 <= ny < row and 0 <= nx < col :
            if not visited[maps[ny][nx]] :
                visited[maps[ny][nx]] = 1
                dfs([ny, nx], depth + 1)
                visited[maps[ny][nx]] = 0
                # visited_letters.pop()

        
dfs([0,0], 1)
print(max_step)




