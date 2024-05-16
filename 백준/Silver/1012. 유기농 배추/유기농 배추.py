T = int(input())

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(y, x):
    stack = [(y,x)]
    
    while stack:
        cy, cx = stack.pop()
        for dy, dx in directions:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                stack.append((ny, nx))

def count_worms(maps):
    cnt = 0
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 1:
                dfs(y,x)
                cnt += 1
    return cnt
                
                
                
    


for _ in range(T):
    M, N, K = map(int, input().split())
    coords = [list(map(int, input().split())) for _ in range(K)]

    maps = [[0 for _ in range(M)] for _ in range(N)]
    for x, y in coords:
        maps[y][x] = 1
        
    print(count_worms(maps))