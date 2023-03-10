## DFS 스페셜 저지
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

test_case = list(map(int, input().split()))    

visited = [0 for _ in range(N+1)]
level = [0 for _ in range(N+1)]
tsize = [0 for _ in range(N+1)]

def dfs(x, depth) :
    if visited[x] :
        return 0
    visited[x] = 1
    size = 1
    level[x] = depth

    for i in graph[x] :
        size += dfs(i, depth + 1)
    tsize[x] = size

    return size


wrong = False
if test_case[0] != 1 :
    print('0')
    wrong = True
else :
    dfs(1,0)
    for i in range(1, N) :
        x = test_case[i]
        if tsize[x] == 1 or i + tsize[x] >= N :
            continue
        nxt = test_case[i + tsize[x]]
        if level[nxt] > level[x] :
            print(0)
            wrong = True
if not wrong :
    print(1)