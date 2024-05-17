'''
백준 1697번 : Hide and Seek
'''
from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    exit()

time = [-1 for _ in range(K*2)]
visited = [0 for _ in range(K*2)]

def bfs(x):
    cnt = 0
    time[x] = cnt
    visited[x] = 1
    if x == K:
        min_cnt = min(min_cnt, cnt)
        return
    if x > K:
        min_cnt = min(min_cnt, cnt + (x - K))
        return
    queue = deque([x])   
    
    while queue:
        cx = queue.popleft()
        for new_x in [ cx*2, cx-1, cx+1]:
            if 0 <= new_x < K*2:
                if not visited[new_x]:
                    visited[new_x] = 1
                    time[new_x] = time[cx] + 1
                    queue.append(new_x)

    
bfs(N)
print(time[K])