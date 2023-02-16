## 사탕 게임

N = int(input())

board = []
for _ in range(N) :
    board.append(list(input()))

def count_candy() :
    row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9

    for i in range(N) :
        for j in range(N-1) :
            if board[i][j] == board[i][j+1] :
                row_cnt += 1
            else :
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    for j in range(N) :
        for i in range(N-1) :
            if board[i][j] == board[i+1][j] :
                col_cnt += 1
            else :
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1

    answer = max(row_max, col_max)
    return answer


directions = [(0,1), (0,-1), (1,0), (-1,0)]

max_value = 0

if max_value == N :
    print(max_value)
else :
    for j in range(N) :
        for i in range(N) :
            for move in directions :
                
                y, x = move
                if (-1 < j+y < N) and (-1 < i+x < N):
                    if board[j][i] != board[j+y][i+x] : 
                        # print(f'j : {j}, i : {i}, move : {move}') 
                        board[j][i], board[j+y][i+x] = board[j+y][i+x], board[j][i]
                        color_dict = {}
                        max_value = max(max_value, count_candy())
                    # for b in board :
                    #     print(b)
                    # print('\n')
                        board[j][i], board[j+y][i+x] = board[j+y][i+x], board[j][i]

    print(max_value)




                        
