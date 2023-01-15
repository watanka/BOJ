## 색종이

N = int(input())

board = [[0 for _ in range(100)] for _ in range(100)]

area = 0

for _ in range(N) :
    x0, y0 = map(int, input().split())
    x0 -= 1
    y0 -= 1

    x1 = min(x0 + 10, 99)
    y1 = min(y0 + 10, 99)
    for col in range(y0, y1) :
        for row in range(x0, x1) :
            if board[col][row] == 0 :
                board[col][row] = 1
                area += 1
print(area)