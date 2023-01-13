## 베르트랑 공준
def is_prime_num(n) :
    arr = [True] * (n+1)
    arr[0], arr[1] = False, False

    for i in range(2, n+1) :
        if arr[i] :
            j = 2

            while i*j <= n :
                arr[i*j] = False
                j+= 1
    return arr

while True :
    N = int(input())
    if N == 0 : break

    prime_mask = is_prime_num(N*2)
    cnt = 0
    for i in range(N+1, N*2+1) :
        if prime_mask[i] :
            cnt += 1
    print(cnt)