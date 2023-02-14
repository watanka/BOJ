## 가장 큰 증가 부분 수열

N = int(input())
nums = list(map(int, input().split()))

dp = nums.copy()#[0 for _ in range(N)]

for i in range(1, N) :
    for j in range(i) :
        if nums[j] < nums[i] :
            dp[i] = max(dp[j] + nums[i], dp[i])

print(max(dp))