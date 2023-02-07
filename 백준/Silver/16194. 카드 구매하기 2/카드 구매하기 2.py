## 카드 구매하기 2

N = int(input())
prices = [0] + list(map(int, input().split()))
dp = prices

for i in range(1, N+1) :
    for j in range(1, i+1) :
        dp[i] = min(dp[i], dp[i-j] + prices[j])
print(dp[N])