## 팩토리얼 0의 개수

N = int(input())
num_ls = range(1, N+1)

div2 = 0
div5 = 0
for num in num_ls :
    dnum2 = num 
    dnum5 = num
    while dnum2 % 2 == 0 :
        dnum2 /= 2
        div2 += 1
    
    while dnum5 % 5 == 0 :
        dnum5 /= 5
        div5 += 1
print(min(div2, div5))

