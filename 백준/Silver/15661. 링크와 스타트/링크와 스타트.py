## 링크와 스타트
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = 100*20

visited = [0] * N
def score() :
    global min_diff
        # print(visited)
    stat1, stat2 = 0, 0
    for i in range(N-1) :
        for j in range(i+1, N) :
            if visited[i] and visited[j] :
                stat1 += S[i][j] + S[j][i]
            elif visited[i] == 0 and visited[j] == 0 :
                stat2 += S[i][j] + S[j][i]
    min_diff = min(min_diff, abs(stat1 - stat2))
    
def recur(target) :
    if target == N :
        score()
        return

    visited[target] = 1
    recur(target + 1)
    visited[target] = 0
    recur(target + 1)


recur(0)
print(min_diff)
