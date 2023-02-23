## 스타트와 링크

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 능력치 계산
def calc_stat(ls) :
    stats = 0
    for i in ls :
        for j in ls :
            if i != j :
                stats += S[i][j]
    return stats


# 팀 조합

visited = [0 for _ in range(N)]
min_cost = 380*100 // 2 + 1
def dfs(start, depth) :
    global min_cost
    if depth  == N//2 :
        stat1, stat2 = 0, 0
        for i in range(N) :
            for j in range(N) :
                if visited[i] and visited[j] :
                    stat1 += S[i][j]
                elif not visited[i] and not visited[j] :
                    stat2 += S[i][j]
        # print(*stack, abs(stat1-stat2))
        min_cost = min(min_cost, abs(stat1 - stat2))
        return

    for i in range(start, N) :
        if not visited[i] :           
            visited[i] = 1
            dfs(i, depth + 1 )
            visited[i] = 0

dfs(0, 0)
print(min_cost)