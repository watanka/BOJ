## 가장 긴 바이토닉 부분 수열

N = int(input())

nums = list(map(int, input().split()))

dp_forward = [1 for _ in range(N)]
dp_backward = [1 for _ in range(N)]

for i in range(1, N) :
    for j in range(i) :
        if nums[i] > nums[j] :
            dp_forward[i] = max(dp_forward[i], dp_forward[j] + 1)

for i in range(N-1, -1, -1) :
    for j in range(N-1, i, -1) :
        if nums[i] > nums[j] :
            dp_backward[i] = max(dp_backward[i], dp_backward[j] + 1)

dp = [dp_forward[i] + dp_backward[i]-1 for i in range(N)]


print(max(dp))
