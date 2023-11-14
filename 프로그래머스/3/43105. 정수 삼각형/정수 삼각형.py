def solution(triangle):
    
    height = len(triangle)
    
    dp = [[0 for _ in range(i+1)] for i in range(height)]
    dp[0][0] = triangle[0][0]
    for level in range(1, height) :
        for idx in range(level + 1) :
            
            above_idx_start = max(0, idx - 1)
            above_idx_end = min(idx, level)
            dp[level][idx] = triangle[level][idx] + max(dp[level - 1][above_idx_start : above_idx_end+1])
        
            
    return max(dp[-1])
        
        
        
    
#     answer = 0
#     return answer