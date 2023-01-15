## 수 정렬하기

N = int(input())

ls = [int(input()) for _ in range(N)]

minval = 100000
min_idx = 0
for i in range(0, len(ls)-1) :
    for j in range(i+1, len(ls)) :
        if ls[i] > ls[j] : 
            tmp = ls[i]
            ls[i] = ls[j]
            ls[j] = tmp
for l in ls :
    print(l)