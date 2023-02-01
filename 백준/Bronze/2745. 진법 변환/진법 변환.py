## 진법 변환

num_exps = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_exps_dict = {exp : dec for dec, exp in enumerate(num_exps)}
N, B = input().split()

B = int(B)
num_list = list(N)

i = 0
result = 0
while num_list :
    trg = num_list.pop()
    result += num_exps_dict[trg] * (B**i)
    i += 1

print(result)