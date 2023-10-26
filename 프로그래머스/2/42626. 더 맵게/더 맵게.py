import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True :
        if len(scoville) == 1 and scoville[0] < K :
            return -1
        
        a = heapq.heappop(scoville)
        
        if a < K :
            b = heapq.heappop(scoville)
            new = a + b * 2
            heapq.heappush(scoville, new)
            cnt += 1
        else :
            return cnt
    
    
    