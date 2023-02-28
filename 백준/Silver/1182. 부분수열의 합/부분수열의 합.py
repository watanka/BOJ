## 부분수열의 합
N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
stack = []

def subset_sum(idx, total) :
    global cnt
    if idx == N :
        return
    
    total += nums[idx] 
    if total == S :
        cnt += 1

    subset_sum(idx+1, total)
    subset_sum(idx+1, total - nums[idx])

subset_sum(0, 0)

print(cnt)