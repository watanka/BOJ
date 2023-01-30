## 최대공약수와 최소공배수

a, b = map(int, input().split())

divider = min(a,b) 
dividee = max(a,b)

def get_gcd(a,b) :
    while b > 0 :
        a,b = b, a%b
    return a

gcd= get_gcd(divider, dividee)

print(gcd)
print(int(a*b/gcd))