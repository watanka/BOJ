## 연결 요소의 개수
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

net = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

visited = [0 for _ in range(N+1)]

# def dfs(node) :
#     stack = []
#     if visited[node] :
#         return 0
#     stack.append(node)

#     while stack :
#         target = stack.pop()
#         visited[target] = 1
#         for cc in net[target] :
#             if not visited[cc] :
#                 visited[cc] = 1
#                 stack.append(cc)

#     return 1

def bfs(start) :
    queue = deque([start])
    visited[start] = 1
    while queue :
        node = queue.popleft()
        for i in net[node] :
            if not visited[i] :
                visited[i] = 1
                queue.append(i)

total = 0
for i in range(1, N+1) :
    if not visited[i] :
        if not net[i] :
            total += 1
            visited[i] = True
        else :
            bfs(i)
            total += 1

    
print(total)
    