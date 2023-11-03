from collections import deque

def solution(begin, target, words):
    
    def diff_by_one(word1, word2) :
        cnt = 0
        for c1, c2 in zip(word1, word2) :
            if c1 != c2 :
                cnt += 1
                if cnt > 1 :
                    return False
        return True
    
    visited = [0 for _ in range(len(words))]
    found = False
    
    trg_idx = 0
    for i, word in enumerate(words) :
        if word == target :
            found = True
            trg_idx = i
            visited[i] = 1
            
    if not found :
        return 0
    
    
    def bfs() :
        nonlocal trg_idx
        queue = deque([(target, trg_idx)])
        
        while queue :
            trg, trg_idx = queue.popleft()
            
            for i, word in enumerate(words) :
                if visited[i] == 0 and diff_by_one(word, trg) :
                    visited[i] = visited[trg_idx] + 1
                    queue.append([word, i])
                    
            
        
    bfs()
    answer = 51
    found = False
    for i, word in enumerate(words) :
        if diff_by_one(word, begin) :
            answer = min(answer, visited[i])
            found = True
            
    return answer if found else 0
    
        