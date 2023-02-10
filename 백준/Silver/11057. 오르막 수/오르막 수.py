## 오르막 수
N = int(input())

dp = [[1 for _ in range(10)] for _ in range(N+1)]

for i in range(2, N+1) :
    prev_sum = sum(dp[i-1])
    dp[i][0] = prev_sum 
    for j in range(1, 10) : 
        dp[i][j] = dp[i][j-1]-dp[i-1][j-1]

# print(dp)
print(sum(dp[N])% 10007)