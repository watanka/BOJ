## 카잉 달력

def gcd(a,b) :
    while b :
        a, b = b, a%b
    return a

T = int(input())
for _ in range(T) :
    M, N, x, y = map(int, input().split())

    lcm = M*N//gcd(M,N)

    max_i = lcm // M
    max_j = lcm // N
    found = False
    for i in range(max_i) :
        if (M*i + x - y) % N == 0 :
            found = True
            print(M*i + x)
    if not found :
        print(-1)