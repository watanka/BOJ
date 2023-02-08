## 가장 긴 증가하는 부분 수열

N = int(input())

num_list = list(map(int, input().split()))
dp = [1 for _ in range(len(num_list))]

for i in range(len(num_list)) :
    for j in range(i) :
        if num_list[i] > num_list[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))