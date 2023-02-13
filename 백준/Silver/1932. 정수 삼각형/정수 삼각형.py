## 정수 삼각형
N = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0] = list(map(int, input().split()))
for i in range(1, N) :
    nums = list(map(int, input().split()))
    
    for j in range(i+1) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + nums[j]
        if j == i :
            dp[i][j] = dp[i-1][j-1] + nums[j]
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] ) + nums[j]

print(max(dp[-1]))