## 숨바꼭질 4
import sys
from collections import deque

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
move = [0 for _ in range(100001)]

def path(x) :
    path_hist = []
    tmp = x
    for _ in range(visited[x] + 1) :
        path_hist.append(tmp)
        tmp = move[tmp]
    return path_hist[::-1]

def bfs(start) :
    queue = deque([start])

    while queue :
        pos = queue.popleft()

        if pos == K :
            return 

        for nxt in (pos-1, pos+1, pos*2) :
            if 0<= nxt <= 100000 and not visited[nxt] :
                queue.append(nxt)
                visited[nxt] = visited[pos] + 1
                move[nxt] = pos
                

bfs(N)

# if N > K :
#     print(N-K)
#     print(*list(range(N,K-1,-1)))
# elif N == K :
#     print(0)
#     print('')
# else :
bfs(N)
print(visited[K])
print(*path(K))




