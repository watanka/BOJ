## 제곱수의 합
N = int(input())

dp = [i for i in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, i+1) :
        if j*j > i :
            break
        if dp[i] > dp[i - j*j] + 1 :
            dp[i] = dp[i - j*j] + 1

print(dp[-1])

