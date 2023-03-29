from collections import deque

def solution(progresses, speeds):
    schedules = deque()
    for prog, speed in zip(progresses, speeds) :
        day = (100 - prog) // speed 
        day += 1 if (100 - prog) % speed else 0
        schedules.append(day)
    
    compare = schedules[0]
    answer = []
    cnt = 0
    while schedules :
        day = schedules.popleft()
        
        if day <= compare :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            compare = day
    if compare < day :
        answer[-1] += 1
    else :
        answer.append(cnt)
    return answer        
        
        
    
            
    return answer
            
    
    