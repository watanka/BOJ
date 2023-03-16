## 트리의 지름
from collections import deque
V = int(input())

tree = [[] for _ in range(V+1)]


for _ in range(V) :
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info)-2, 2) :
        neighbor, dist = info[i:i+2]
        tree[node].append((neighbor, dist))

def bfs(start) :
    queue = deque([start])
    visited[start] = 0
    max_value = [0, 0]

    while queue :
        node = queue.popleft()
        for (neighbor, dist) in tree[node] :
            if visited[neighbor] == -1 :
                visited[neighbor] = visited[node] + dist
                queue.append(neighbor)
                if max_value[0] < visited[neighbor] :
                    max_value = (visited[neighbor], neighbor)
    return max_value    

visited = [-1 for _ in range(V+1)]
dis, node = bfs(1)
visited = [-1 for _ in range(V+1)]
dis, node = bfs(node)
print(dis)