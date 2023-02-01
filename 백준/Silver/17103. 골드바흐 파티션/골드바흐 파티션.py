## 골드바흐 파티션
T = int(input())

def get_prime_list(N) :

        mask = [1 for _ in range(N+1)]
        mask[0] = 0
        mask[1] = 0
        i = 2
        while i < N**(1/2) + 1 :
            if mask[i] :
                j = 2
                while i* j <= N :
                    mask[i*j] = 0
                    j += 1
            i += 1
        return mask

prime_list = get_prime_list(1000000)


for _ in range(T) :

    N = int(input())

    

    cnt = 0
    for i in range(2, N // 2 + 1) :
        if prime_list[i] and prime_list[N-i] :
            cnt += 1
    print(cnt)
