## 수 정렬하기

# 선택 정렬
N = int(input())

ls = [int(input()) for _ in range(N)]

minval = 100000
min_idx = 0
for i in range(0, len(ls)-1) :
    for j in range(i+1, len(ls)) :
        if ls[i] > ls[j] : 
            ls[i], ls[j] = ls[j], ls[i]
for l in ls :
    print(l)