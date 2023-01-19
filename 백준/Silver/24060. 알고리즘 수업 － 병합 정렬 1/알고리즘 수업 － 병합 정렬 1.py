## 병합 정렬

def merge_sort(arr) :
    
    length = len(arr)
    if length == 1 :
        return arr
    
    middle = (length + 1) // 2
    
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    sorted_left = merge_sort(left_arr)
    sorted_right = merge_sort(right_arr)
    
    sorted_nums = []
    idx_l, idx_r = 0, 0
    
    while idx_l < len(sorted_left) and idx_r < len(sorted_right) :
        if sorted_left[idx_l] < sorted_right[idx_r] :
            sorted_nums.append(sorted_left[idx_l])
            ans.append(sorted_left[idx_l])
            idx_l += 1
        else : 
            sorted_nums.append(sorted_right[idx_r])
            ans.append(sorted_right[idx_r])
            idx_r += 1
    while idx_l < len(sorted_left) :
        sorted_nums.append(sorted_left[idx_l])
        ans.append(sorted_left[idx_l])
        idx_l += 1
    while idx_r < len(sorted_right) :
        sorted_nums.append(sorted_right[idx_r])
        ans.append(sorted_right[idx_r])
        idx_r += 1
    
    return sorted_nums
        
        
ans = []
   
N, k = map(int, input().split())
arr = list(map(int, input().split()))

merge_sort(arr)

if len(ans) >= k :
    print(ans[k-1])
else :
    print(-1)
