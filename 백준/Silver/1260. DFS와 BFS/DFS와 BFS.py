from collections import deque

N, M, V = map(int, input().split(' '))

relations = [map(int, input().split(' ')) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for start, end in relations:
    graph[start].append(end)
    graph[end].append(start)

for i in range(len(graph)):
    graph[i].sort()

# DFS
def dfs(start_node):
    visited = []
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node][::-1])

    return visited


# BFS

def bfs(start_node):
    visited = []
    q = deque([start_node])
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    return visited

print(*dfs(V))
print(*bfs(V))
