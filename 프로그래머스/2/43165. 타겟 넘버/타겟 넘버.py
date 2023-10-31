def solution(numbers, target):
    answer = 0
    
    N = len(numbers)
    
    def dfs(idx, result) :
        nonlocal answer
        if idx == N - 1 :
            if result == target :
                answer += 1
            return
        
       
        dfs( idx + 1, result + numbers[idx])
        dfs( idx + 1, result - numbers[idx])
            
            
    dfs(-1, 0)
    
    return answer