## 숨바꼭질
import sys
from collections import deque

sys.setrecursionlimit(100000)
N, K = map(int, input().split())


visited = [0 for _ in range(100001)]

if N == K :
    print(0)
    sys.exit()
if N > K :
    print(N-K)
    sys.exit()
else :
    min_pt, max_pt = [0,  100000]

def bfs(x) :
    queue = deque([x])
    visited[x] = 1

    while queue :
        pos = queue.popleft()
        
        if pos == K :
            return

        if min_pt <= pos + 1 <= max_pt :
            if not visited[pos+1] :
                visited[pos+1] = visited[pos] + 1
                queue.append(pos+1)

        if min_pt <= pos - 1 <= max_pt :
            if not visited[pos-1] :
                visited[pos-1] = visited[pos] + 1
                queue.append(pos-1)

        if min_pt <= pos * 2 <= max_pt :
            if not visited[pos*2] :
                visited[pos*2] = visited[pos] + 1
                queue.append(pos*2)



bfs(N)

print(visited[K]-1)