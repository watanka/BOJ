## 트리의 지름 1967
import sys
sys.setrecursionlimit(1000000)

N = int(input())

tree = [[] for _ in range(N+1)]
r_list = [0 for _ in range(N+1)]
for _ in range(N-1) :
    parent, child, edge = map(int, input().split())
    tree[parent].append((child, edge))

ans = 0
def dfs(node, maxdist) :
    global ans
    left, right = 0, 0
    for child, dist in tree[node] :
        r = dfs(child, dist)
        if left <= right :
            left = max(left, r)
        else :
            right = max(right, r)
        
    
    ans = max(ans, left + right)
    
    return max(left + maxdist, right+maxdist)

dfs(1,0)
print(ans)

                
