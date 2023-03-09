## 서울 지하철 2호선
import sys
from collections import deque
sys.setrecursionlimit(10000)

N = int(input())


lines = [[] for _ in range(N+1)]
for _ in range(N) :
    a,b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)


def dfs(node, cnt, end_node) : 
    global cycle
    if node == end_node and cnt >= 2 :
        cycle = True
        return
    visited[node] = 1

    for i in lines[node] :
        if not visited[i] :
            dfs(i, cnt+1, end_node)
        elif i == end_node and cnt >= 2 :
            dfs(i, cnt, end_node)
        

def bfs(node) :
    queue = deque([node])
    dist[node] = 1

    while queue :
        snode = queue.popleft()

        for i in lines[snode] :
            if cycle_station[i] :
                return dist[snode] 
            if not dist[i] :
                dist[i] = dist[snode] + 1
                queue.append(i)
    return -1




cycle_station = [0 for _ in range(N+1)]


for i in range(1, N+1) :
    visited = [0 for _ in range(N+1)]
    cycle = False
    dfs(i, 0, i)
    if cycle :
        cycle_station[i] = 1

ans = []
for i in range(1, N+1) :
    if cycle_station[i] :
        ans.append(0)
    else : 
        dist = [0 for _ in range(N+1)]
        ans.append(bfs(i))

print(*ans)
    





