def solution(priorities, location):
    
    popval = 0
    indices = [i for i in range(len(priorities))]
    result = []
    while priorities :
        p = priorities.pop(0)
        i = indices.pop(0)
        if len(priorities) > 0 and p < max(priorities) :
            priorities.append(p)
            indices.append(i)
        else :
            result.append(i)
        
    
    return result.index(location) + 1
            
        
        
        
        
    
    
    
    
    