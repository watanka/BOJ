## 섬의 개수
import sys
sys.setrecursionlimit(50*50)
moves = [[1,0], [-1,0], [0,-1], [0,1], [-1,-1], [-1, 1], [1, -1], [1, 1]]
def dfs(y,x) :

    if island_map[y][x] == 0:
        return False

    island_map[y][x] = 0
    for mv in moves :
        h,w = mv
        ny, nx = y+h, x+w
        if 0 <= nx < W and 0 <= ny < H :
            dfs(ny, nx)
    return True









while True :
    W, H = map(int, input().split())
    if W == 0 and H == 0 :
        break

    island_map = []
    cnt = 0
    for _ in range(H) :
        island_map.append(list(map(int, input().split())))
    
    for j in range(H) :
        for i in range(W) :
            if dfs(j, i) :
                cnt += 1
            
    print(cnt)
    