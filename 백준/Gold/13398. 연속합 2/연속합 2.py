N = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(2)]

dp[0][0] = nums[0]
dp[1][0] = -1e9

if N == 1 :
    print(nums[0])
else :
    for i in range(1, N) :
        dp[0][i] = max(dp[0][i-1] + nums[i], nums[i])
        dp[1][i] = max(dp[1][i-1] + nums[i], dp[0][i-1])

    print(max(max(dp[0]), max(dp[1])))