## 골드바흐의 추측

T = int(input())

def is_prime_num(n) :

    arr = [True] * (n+1)
    arr[0], arr[1] = False, False

    for i in range(2, n+1) :
        if arr[i] :
            j = 2
            while i * j <= n :
                arr[i*j] = False
                j+=1

    return arr


for _ in range(T) :
    N = int(input())

    prime_mask = is_prime_num(N)

    start_idx = N // 2

    for p1 in range(start_idx, 1, -1) :
        if prime_mask[p1] and prime_mask[N-p1] :
            print(p1, N-p1)
            break

    
        

