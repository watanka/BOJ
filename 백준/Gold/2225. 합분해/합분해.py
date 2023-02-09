## 합분해

N, K = map(int, input().split())

dp = [[i for i in range(K+1)] for _ in range(N+1)]

for i in range(2, N+1) :
    for j in range(2, K+1) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][K] % 1000000000)