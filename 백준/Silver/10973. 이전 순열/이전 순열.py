## 이전 순열
N = int(input())
nums = list(map(int, input().split()))

find = False
for i in range(N-1, 0, -1) :
    if nums[i] < nums[i-1] :
        for j in range(N-1, 0, -1) :
            if nums[j] < nums[i-1] :
                nums[j], nums[i-1] = nums[i-1], nums[j]
                find = True
                
                nums = nums[:i] + sorted(nums[i:], reverse = True)
                break
    if find :
        print(*nums)
        break

if not find :
    print(-1)