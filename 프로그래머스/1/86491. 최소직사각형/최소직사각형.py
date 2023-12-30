def solution(sizes):
    # 가로길이, 세로길이 상관없이 가장 긴 길이는 무조건 필요
    # 가장 긴 길이는 첫번째 loop에서 max_long으로 저장.
    # 더 짧은 길이 중 최대 길이를 max_short에 저장.
    
    max_long = 0
    max_short = 0
    for width, height in sizes :
        max_long = max(width, height, max_long)
    
    for width, height in sizes :
        shorter = min(width, height)
        max_short = max(shorter, max_short)
        
    return max_long * max_short
        
        
            
        
        
        
    
    