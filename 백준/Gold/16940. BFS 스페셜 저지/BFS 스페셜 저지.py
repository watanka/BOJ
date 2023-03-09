## BFS 스페셜 저지
from collections import deque

N = int(input())

visited = [0 for _ in range(N+1)]
visited_case = [set() for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = list(map(int, input().split()))


def bfs(start) :
    queue = deque([start])
    visited[start] = 1

    while queue :
        x = queue.popleft()

        for y in graph[x] :
            if not visited[y] :
                visited[y] = visited[x] + 1
                visited_case[x].add(y)
                queue.append(y)

bfs(1)

idx = 1
wrong = False
for i in result :
    if idx == N :
        break
    c_length = len(visited_case[i])
    candidate1 = set(result[idx : idx + c_length])
    candidate2 = visited_case[i]
    if candidate1 != candidate2 :
        print(0)
        wrong = True
        break
    idx += c_length
if not wrong :
    print(1)