def solution(arr):
    
    last = arr[0]
    answer = [last]
    for i in range(1, len(arr)) :
        if arr[i] != last :
            answer.append(arr[i])
            last = arr[i]
            
    return answer
        
        