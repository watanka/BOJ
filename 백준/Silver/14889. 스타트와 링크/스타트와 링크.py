## 스타트와 링크
import sys

N = int(input())
stats = []
for _ in range(N) :
    stats.append(list(map(int, input().split())))

min_diff = sys.maxsize

def calculate_diff() :
    start_score = 0
    link_score = 0
    for j in range(N) :
        for i in range(N) :
            if visited[i] and visited[j] :
                start_score += stats[i][j]
            elif not visited[i] and not visited[j] :
                link_score += stats[i][j]
    return abs(start_score - link_score)



visited = [0 for _ in range(N)]
def dfs(depth, start) :
    global min_diff
    if depth == N//2 :
        min_diff = min(min_diff, calculate_diff())
        return

    for i in range(start, N) :
        if not visited[i] :
            visited[i] = 1
            dfs(depth+1, i)
            visited[i] = 0

dfs(0, 0)
print(min_diff)
