## N-Queen

N = int(input())

cnt = 0
def dfs(depth) :
    global cnt
    if depth == N :
        cnt += 1
        return

    for i in range(N) :
        if not visited[i] :
            graph[depth] = i

            t = True
            for j in range(depth) :
                if abs(graph[depth] - graph[j]) == abs(depth - j) :
                    t = False
                    break
            if t :
                visited[i] = 1
                dfs(depth + 1)
                visited[i] = 0

graph = [0 for _ in range(N)]
visited = [0 for _ in range(N)]

dfs(0)
print(cnt)