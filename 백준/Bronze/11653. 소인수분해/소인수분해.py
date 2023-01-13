## 소인수분해

N = int(input())

div = 2


while True :
    while N % div == 0 :
        print(div)
        N = N / div 
    if N == 1 :
        break

    if N > div :
        div += 1
    