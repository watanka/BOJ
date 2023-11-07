import collections

def solution(tickets):
    answer = []
    
    routes = collections.defaultdict(list)
    
    for ticket in tickets :
        departure, arrival = ticket
        routes[departure].append(arrival)
    
    for airport in routes :
        routes[airport].sort(reverse = True)
    
    def dfs(airport) :
        stack = [airport]
        
        while stack :
            while routes[stack[-1]] :
                stack.append(routes[stack[-1]].pop())
            answer.append(stack.pop())
        
    dfs('ICN')
        
    return answer[::-1]