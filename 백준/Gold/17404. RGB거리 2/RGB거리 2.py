## RGB거리 2
N = int(input())



costs = [[-1,-1,-1]]
for _ in range(N) :
    costs_by_color = list(map(int, input().split()))
    costs.append(costs_by_color)

INF = 1000*1000 + 1

answer = INF
for color in range(3) :
    dp = [[-1 for _ in range(3)] for _ in range(N+1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = costs[1][color]

    for i in range(2, N+1) :
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
    dp[-1][color] = INF
    answer = min(answer, min(dp[-1]))

print(answer)