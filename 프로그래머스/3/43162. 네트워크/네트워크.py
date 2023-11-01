def solution(n, computers):
    
    answer = 0
    def dfs(computer) :
        visited[computer] = True
        
        for i in range(n) :
            if computers[computer][i] == 1 and not visited[i] :
                dfs(i)
    
    visited = [False for _ in range(n)]
    for i in range(n) :
        if not visited[i] :
            dfs(i)
            answer += 1
    
    return answer