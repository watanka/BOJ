from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0 
    if cacheSize == 0 :
        return 5*len(cities)
    
    for city in cities :
        city = city.lower()
        
        if city not in cache :
            time += 5
        else : 
            time += 1
        
        if city in cache:
            cache.remove(city)
        if len(cache) >= cacheSize :
            cache.pop()
        
        cache.appendleft(city)
            
        
    return time