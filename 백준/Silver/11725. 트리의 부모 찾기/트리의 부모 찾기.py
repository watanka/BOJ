## 트리의 부모 찾기
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# bfs

visited = [0 for _ in range(N+1)]
queue = deque([1])

tree = [0 for _ in range(N+1)]

while queue :
    parent = queue.popleft()
    visited[parent] = 1
    for child in graph[parent] :
        if not visited[child] :
            tree[child] = parent
            queue.append(child)
            
for i in range(2, N+1):
    print(tree[i])
