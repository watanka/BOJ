## 스도쿠
N = 9
board = [[0 for _ in range(N)] for _ in range(N)]

blanks = []
for j in range(N) :
    nums = list(map(int, input().rstrip().split()))
    for i in range(N) :
        if nums[i] == 0 :
            blanks.append((j,i))
        board[j][i] = nums[i]


def check(pos, num) :
    y, x = pos
    # vertical
    for j in range(N) :
        if board[j][x] == num :
            return False
    # horizontal
    for i in range(N) :
        if board[y][i] == num :
            return False
    
    # grid
    ny = y // 3 * 3
    nx = x // 3 * 3
    for j in range(3) :
        for i in range(3) :
            if board[ny+j][nx+i] == num :
                return False
    
    return True

def dfs(idx) :
    
    if idx == len(blanks) :
        for b in board :
            print(*b)
        exit(0)

    for i in range(1, 10) :
        y = blanks[idx][0]
        x = blanks[idx][1]

        if check((y,x), i) :
            board[y][x] = i
            dfs(idx+1)
            board[y][x] = 0

dfs(0)

        
    

        

        

    

