## 이모티콘
import sys
from collections import deque

S = int(input())

visited = [[0 for _ in range(6001)] for _ in range(6001)]
def bfs() :
    screen = 1
    clipboard = 0
    queue = deque([(clipboard, screen)])
    visited[clipboard][screen] = 1

    while queue :
        clipboard, screen = queue.popleft()
        

        for opt_clipboard, opt_screen in [(screen, screen), (clipboard, clipboard + screen), (clipboard, screen - 1)] :
            if opt_clipboard == 0 and opt_screen == 0 :
                continue
            if opt_clipboard >= 0 and opt_screen >= 0 :
                if not visited[opt_clipboard][opt_screen] :
                    visited[opt_clipboard][opt_screen] = visited[clipboard][screen] + 1
                    queue.append((opt_clipboard, opt_screen))

                if opt_screen == S :
                    
                    return

bfs()

min_sec = sys.maxsize
for v in visited :
    if v[S] != 0 and min_sec > v[S] :
        min_sec = v[S]
        break
print(min_sec-1)
            
