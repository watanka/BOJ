## RGB 거리
N = int(input())

dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, len(dp)) :
    neighbor = dp[i-1]
    for color in range(3) :

        dp[i][color] = dp[i][color] + min([neighbor[c] for c in range(3) if c != color])

print(min(dp[-1]))

