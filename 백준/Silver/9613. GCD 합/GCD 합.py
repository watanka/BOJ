## GCD 합

N = int(input())

def get_gcd(a, b) :

    while b > 0 :
        a,b = b, a%b
    return a


for _ in range(N) :
    num_ls = list(map(int, input().split()))[1:]
    total = 0
    for i in range(len(num_ls)-1) :
        for j in range(i+1, len(num_ls)) :
            gcd = get_gcd(num_ls[i], num_ls[j])
            total += gcd
    
    print(total)