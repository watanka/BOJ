## DFS와 BFS

N, M, V = map(int, input().split())
net = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

for i in range(len(net)) :
    net[i].sort()


def dfs(start_node) :
    stack = []
    visited = []
    stack.append(start_node)

    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
            stack.extend(net[node][::-1])

    return visited



def bfs(start_node) :
    queue = []
    visited = []
    queue.append(start_node)
    while queue :
        node = queue.pop(0)
        if node not in visited :
            visited.append(node)
            queue.extend(net[node])

    return visited

print(*dfs(V))
print(*bfs(V))