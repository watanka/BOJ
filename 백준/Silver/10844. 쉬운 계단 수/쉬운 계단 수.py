N = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, 101) :
    for j in range(10) :
        left = dp[i-1][j-1] if j>0 else 0
        right = dp[i-1][j+1] if j<9 else 0
        dp[i][j] = left+right


print(sum(dp[N]) % 1000000000)