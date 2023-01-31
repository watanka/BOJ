## 숨바꼭질
N, S = map(int, input().split())
positions = list(map(int, input().split()))

def get_gcd(a,b) :
    while b > 0 :
        a,b = b, a%b
    return a

distances = [abs(pos - S) for pos in positions]

min_dist = min(distances)

result = 10**9
for dist in distances :
    result = min(result, get_gcd(min_dist, dist))

print(result)