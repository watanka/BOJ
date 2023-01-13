## 소수 구하기
M, N = map(int, input().split())

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

prime_mask = is_prime_num(N)
for i in range(M, N+1) :
    if prime_mask[i] :
        print(i)

