T = int(input())
ls = list(map(int, input().split()))

min_num, max_num = ls[0], ls[0]

for v in ls :
    if v < min_num :
        min_num = v
    if v > max_num :
        max_num = v
        
print(f"{min_num} {max_num}")