## 진법 변환 2

num_exps = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())

res = ''
num_exps = num_exps[:B]
# num_exps = num_exps[B-1] + num_exps

while N  :
    res = num_exps[N%B] + res
    N //= B 

print(res)
