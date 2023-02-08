## 가장 긴 증가하는 부분 수열 4
N = int(input())
num_list = list(map(int, input().split()))

dp = [1 for _ in range(len(num_list))]
dp_list = [[num] for num in num_list]

for i in range(len(num_list)) :
    for j in range(i) :
        if num_list[i]>num_list[j] :
            if dp[j] + 1 > dp[i] :
                dp_list[i] = dp_list[j] + [num_list[i]]             
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
print(*max(dp_list, key = lambda x : len(x)))