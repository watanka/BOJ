## 단지번호붙이기

N = int(input())

housemap = []
for _ in range(N) :
    housemap.append(list(map(int, list((input())))))

# housemap = [list(map(int, list('0110100'))),
#             list(map(int, list('0110101'))),
#             list(map(int, list('1110101'))),
#             list(map(int, list('0000111'))),
#             list(map(int, list('0100000'))),
#             list(map(int, list('0111110'))),
#             list(map(int, list('0111000'))),]


moves = [[1,0], [-1,0], [0,-1], [0,1]]
visited = [[0 for _ in range(N)] for _ in range(N)]

color = 1
def bfs(node) :
    global color
    y,x = node
    if visited[y][x] or housemap[y][x] == 0 :
        return 0
    
    visited[y][x] = color
    queue = [node]
    cnt = 1
    while queue :
        h, w = queue.pop(0)
        for mv in moves :
            mv_h, mv_w = mv

            if 0 <= mv_h + h < N and 0 <= mv_w + w < N :
                if not visited[mv_h+h][mv_w+w] and housemap[mv_h+h][mv_w+w] == 1:
                    visited[mv_h+h][mv_w+w] = color
                    queue.append((mv_h + h, mv_w + w))
                    cnt += 1
    color += 1
    return cnt
    

cnt_ls = []
for j in range(N) : # height
    for i in range(N) : # width 
        cnt = bfs((j,i))
        if cnt :
            cnt_ls.append(cnt)

cnt_ls.sort()

print(color - 1)
for cnt in cnt_ls :
    print(cnt)



        
    

