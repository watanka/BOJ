## 숨바꼭질 3
from collections import deque

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
dist = [-1 for _ in range(100001)]

def bfs() :
    queue = deque([N])
    visited[N] = 1
    dist[N] = 0

    while queue :
        pos = queue.popleft()
        if pos == K :
            return
        for nxt in [pos+1, pos-1, pos*2] :
            if 0 <= nxt < 100001 :
                if not visited[nxt] :
                    if nxt == pos*2 :
                        queue.appendleft(nxt)
                        visited[nxt] = 1
                        dist[nxt] = dist[pos]
                    else :
                        queue.append(nxt)
                        visited[nxt] = 1
                        dist[nxt] = dist[pos] + 1
            
                
    

if N >= K :
    print(N-K)
else :
    bfs()
    print(dist[K])
    