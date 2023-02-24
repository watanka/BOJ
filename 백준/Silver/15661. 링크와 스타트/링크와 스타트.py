## 링크와 스타트
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

num_players = N//2
min_diff = 100*20


def dfs(L, start, cnt) :
    global min_diff
    if cnt == L :
        stat1, stat2 = 0, 0
        for i in range(N-1) :
            for j in range(i+1,N) :
                if visited[i] and visited[j] :
                    stat1 += S[i][j] + S[j][i]
                elif visited[i] == 0 and visited[j] == 0 :
                    stat2 += S[i][j] + S[j][i]
        min_diff = min(min_diff, abs(stat1 - stat2))
        return
    
    for i in range(start, N) :
        if not visited[i] :
            visited[i] = 1
            dfs(L, i+1, cnt+1)
            visited[i] = 0


for num_player in range(1, num_players + 1) :
    visited = [0] * N
    dfs(num_player, 0, 0)

print(min_diff)

