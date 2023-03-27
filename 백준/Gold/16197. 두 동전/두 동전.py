## 두 동전

N, M = map(int, input().split())
coin_locations = []
maps = [[0 for _ in range(M)] for _ in range(N)]
for j in range(N) :
    inp = input()
    for i in range(M) :
        maps[j][i] = inp[i]
        if inp[i] == 'o' :
            coin_locations.append((j, i))

directions = [[0,1], [1,0], [0,-1], [-1,0]]

def fall(location) :
    y, x = location
    if  0 <= y < N and  0 <= x < M :
        return False
    return True

min_move = 11
visited = []
def dfs(coin_locations, move) :
    global min_move
    
    coin1, coin2 = coin_locations
    y1, x1 = coin1
    y2, x2 = coin2

    if x1 == x2 and y1 == y2 :
        return

    if move >= min_move or move > 10 :
        return

    if fall((y1, x1)) and fall((y2, x2)):    
        return
    
    elif (fall((y1, x1)) or fall((y2, x2))) :
        min_move = min(min_move, move)
        return

    for dy, dx in directions :
        coin1, coin2 = coin_locations
        y1, x1 = coin1
        y2, x2 = coin2

        ny1, nx1 = dy + y1 , dx + x1
        ny2, nx2 = dy + y2 , dx + x2

        if 0 <= ny1 < N and 0 <= ny2 < N and 0 <= nx1 < M and 0 <= nx2 < M :
            
            if maps[ny1][nx1] == '#' :
                ny1, nx1 = y1, x1
            
            if maps[ny2][nx2] == '#' :
                ny2, nx2 = y2, x2   
            
            if (ny1, nx1, ny2, nx2) not in visited :
                visited.append([ny1, nx1, ny2, nx2])
                dfs([(ny1, nx1), (ny2, nx2)], move + 1)
                visited.pop()

        else :
            visited.append([ny1, nx1, ny2, nx2])
            dfs([(ny1, nx1), (ny2, nx2)], move + 1)
            visited.pop()

    
dfs(coin_locations, 0)
if min_move > 10 :
    print(-1)
else :
    print(min_move)
