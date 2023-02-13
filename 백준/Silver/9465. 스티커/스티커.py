## 스티커

T = int(input())

for _ in range(T) :
    stickers = []
    N = int(input())

    for _ in range(2) :
        
        stickers.append([0] + list(map(int, input().split())))

    dp = [[stickers[0][i], stickers[1][i]] for i in range(N+1)]


    
    for i in range(2, N+1) :
        dp[i][0] = max(max(dp[i-2]) + stickers[0][i], dp[i-1][1] + stickers[0][i])  
        dp[i][1] = max(max(dp[i-2]) + stickers[1][i], dp[i-1][0] + stickers[1][i])

    
    print(max(dp[-1]))