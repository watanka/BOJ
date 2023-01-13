## 소수
M = int(input())
N = int(input())

prime_total = 0
prime_min = None
for trg in range(M, N+1) :

    if trg == 1 :
        continue

    prime = True
    for div in range(2, trg) :
        if trg % div == 0 :
            prime = False
            break
    if prime :
        if prime_min is None :
            prime_min = trg
        prime_total += trg

if prime_min is None :
    print(-1)      
else :
    print(prime_total)
    print(prime_min)

