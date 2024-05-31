'''
백준 15989 1, 2, 3 더하기 4
'''
T = int(input())

n_list = [int(input()) for _ in range(T)]

limit = 10001

dp = [1 for _ in range(limit)]

for i in range(2, limit):
	dp[i] += dp[i-2]

for i in range(3, limit): 
	dp[i] += dp[i-3]
	


for n in n_list:
	print(dp[n])
