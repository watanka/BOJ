def solution(s):
    
    
    opened = 0
    idx = 0
    
    while idx < len(s) :
        trg = s[idx]
        if trg == '(' :
            opened += 1    
        else : 
            if opened == 0 :
                return False
            opened -= 1
        idx += 1
    return opened == 0
            
        
    