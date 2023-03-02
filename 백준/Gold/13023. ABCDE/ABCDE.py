## ABCDE
N, M = map(int, input().split())

relations = [[] for _ in range(N)]
visited = [0] * 2001
for _ in range(M) :
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

ans = 0
def dfs(idx, depth) :
    global ans
    visited[idx] = True

    if depth == 4 :
        ans = 1
        return

    for i in relations[idx] :
        if not visited[i] :
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0

for i in range(N) :
    dfs(i, 0)
    visited[i] = 0
    if ans :
        break

print(ans)
    
