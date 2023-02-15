## 타일 채우기
N = int(input())

width = N//2
dp = [0 for _ in range(16)]
dp[0] = 1
dp[1] = 3
dp[2] = 11

if N % 2 :
    print(0)
else :
    for i in range(3, width+1) :
        dp[i] = dp[i-1] * 3 + dp[i-2] * 3 - dp[i-3]
    print(dp[width])