## 다리 만들기
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

maps = []
for _ in range(N) :
    maps.append(list(map(int, input().split())))


# maps = [[1,1,1,0,0,0,0,1,1,1],
#         [1,1,1,1,0,0,0,0,1,1],
#         [1,0,1,1,0,0,0,0,1,1],
#         [0,0,1,1,1,0,0,0,0,1],
#         [0,0,0,1,0,0,0,0,0,1],
#         [0,0,0,0,0,0,0,0,0,1],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,1,1,0,0,0,0],
#         [0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0]
#         ]


colors = [[0 for _ in range(N)] for _ in range(N)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(node, color) :
    '''mark island'''
    y, x = node

    if maps[y][x] == 0 or colors[y][x] :
        return False

    colors[y][x] = color
    stack = [node]

    while stack :
        y, x = stack.pop()
        for (dy, dx) in directions :
            ny, nx = y+dy, x+dx
            if (0 <= ny < N) and (0 <= nx < N) :
                if not colors[ny][nx] and maps[ny][nx] == 1 :
                    colors[ny][nx] = color
                    stack.append((ny, nx))
    return True

def bfs(node, color) :
    y, x = node

    if colors[y][x] == color :
        dist[y][x] = 1
    
    queue = deque([node])

    candidates = []
    while queue :
        y,x = queue.popleft()
        visited[y][x] = 1
        for (dy, dx) in directions :
            ny, nx = y+dy, x+dx
            if (0 <= ny < N) and (0 <= nx < N) :
                if not visited[ny][nx] :
                    if colors[ny][nx] != color and colors[ny][nx] != 0 :
                        # found other island
                        dist[ny][nx] = dist[y][x] + 1
                        visited[ny][nx] = 1
                        candidates.append(dist[y][x] + 1)
                        
                    elif colors[ny][nx] == 0 :
                        dist[ny][nx] = dist[y][x] + 1
                        queue.append((ny, nx))
                        visited[ny][nx] = 1

                    elif colors[ny][nx] == color :
                        dist[ny][nx] = 1
                        visited[ny][nx] = 1
                    
                    
    return candidates
    




## DFS로 섬들을 색깔 구분. 결괏값은 visited에 저장.
color = 1
color_list = []
for j in range(N) :
    for i in range(N) :
        if dfs((j,i), color) :
            color_list.append(color)
            color += 1


## 컬러별 다른 섬까지의 거리 BFS 계산
min_dist = sys.maxsize
for color in color_list : 
    
    for j in range(N) :
        for i in range(N) :
            if colors[j][i] == color :
                dist = [[0 for _ in range(N)] for _ in range(N)]
                visited = [[0 for _ in range(N)] for _ in range(N)]
                curr_dists = bfs((j,i), color)     
                # print(curr_dists)
                if len(curr_dists) : 
                    curr_dist = min(curr_dists)

                    min_dist = min(curr_dist, min_dist)


print(min_dist-2)




