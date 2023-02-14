N = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(2)]

dp[0][0] = nums[0]
if N == 1 :
    print(nums[0])
else :
    ans = -1e9
    for i in range(1, N) :
        dp[0][i] = max(dp[0][i-1] + nums[i], nums[i])
        dp[1][i] = max(dp[1][i-1] + nums[i], dp[0][i-1])
        ans = max(ans, dp[0][i], dp[1][i])

    print(ans)