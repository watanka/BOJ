'''
백준 11049 행렬 곱셈 순서
'''

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for distance in range(1, N):
	for start in range(0, N-distance):
		end = start + distance
		if distance == 1:
			dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
			
		dp[start][end] = 2**32 # 최댓값
		for middle in range(start, end):
			num_merge = matrix[start][0] * matrix[middle][1] * matrix[end][1]
			dp[start][end] = min(dp[start][end],
						            dp[start][middle] + dp[middle+1][end] + num_merge)
													
print(dp[0][-1]) # 가장