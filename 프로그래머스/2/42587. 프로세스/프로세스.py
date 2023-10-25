def solution(priorities, location):
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
    
#     p_order = list(sorted(priorities, reverse = True))
#     indices = [i for i in range(len(priorities))]
    
#     num_place = 1
#     while priorities :
#         p = priorities.pop(0)
#         i = indices.pop(0)
        
#         if p == p_order[0] : # 뽑는다.
#             if location == i :
#                 return num_place
#             p_order.pop(0)
#             num_place += 1
#         else : 
#             priorities.append(p)
#             indices.append(i)
        
    
    
    
        
        
        
    
    
    
    
    