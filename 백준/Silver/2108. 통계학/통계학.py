import sys
## 통계학


N = int(input())

num_list = []
median_idx = N // 2
ntotal = 0

for _ in range(N) :
    num = int(sys.stdin.readline())
    num_list.append(num)
    ntotal += num

num_list.sort()

num_cnt = {}

for num in num_list :
    if num not in num_cnt.keys() :
        num_cnt[num] = 1
    else :
        num_cnt[num] += 1

max_cnt = -1
mode_val_ls = []
for num, cnt in num_cnt.items() :
    if cnt > max_cnt :
        max_cnt = cnt
        mode_val_ls = [num]
    elif cnt == max_cnt :
        mode_val_ls.append(num)

mode_val_ls = sorted(mode_val_ls)

if len(mode_val_ls) >= 2 :
    mode_val = mode_val_ls[1]
else :
    mode_val = mode_val_ls[0]
    

print(round(ntotal / N))
print(num_list[median_idx])
print(mode_val)
print(num_list[-1] - num_list[0])