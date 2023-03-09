## 이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)
T = int(input())

def dfs(node, group) :

    visited[node] = group
    for i in net[node] :
        if not visited[i] :
            result = dfs(i, -group)
            if not result :
                return False
        elif visited[i] == visited[node] :
            return False
    return True


for _ in range(T) :
    V, E = map(int, input().split())
    net = [[] for _ in range(V+1)]
    for _ in range(E) :
        a, b = map(int, input().split())
        net[a].append(b)
        net[b].append(a)


    visited = [0 for _ in range(V+1)]
    
    for i in range(1, V+1) :
        if not visited[i] :
            result  = dfs(i, 1)
            if not result :
                break

    print("YES" if result else "NO")
    