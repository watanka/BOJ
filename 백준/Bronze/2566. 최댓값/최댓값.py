## 최댓값

board = []
for _ in range(9) :
    board.append(list(map(int, input().split())))

row = 0
col = 0
maxval = -1

for i in range(9) :
    for j in range(9) :
        if board[i][j] > maxval :
            maxval = board[i][j]
            row = i
            col = j

print(maxval)
print(row+1, col+1)