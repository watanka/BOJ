'''
 백준 1890번 점프
'''

N = int(input())

board = []
for _ in range(N):
	board.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

cnt = 0

for y in range(N):
    for x in range(N):
        if dp[y][x] != 0:
            jump_distance = board[y][x]
            if jump_distance == 0: continue
            next_y, next_x = y + jump_distance, x + jump_distance
            # if (next_y == N-1 and x == N-1) or (next_x == N-1 and y == N-1): # 이동한 곳이 보드의 끝이면
            #     cnt += 1
            if next_y < N: # y축 이동
                dp[next_y][x] += dp[y][x]
            if next_x < N: # x축 이동
                dp[y][next_x] += dp[y][x]              
				
print(dp[-1][-1])