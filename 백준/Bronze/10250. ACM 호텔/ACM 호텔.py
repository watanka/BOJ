## ACM 호텔

T = int(input())

for _ in range(T) :
    H, W, N = map(int, input().split())
    
    X = -(-N // H)
    Y = N % H
    if Y == 0 :
        Y = H
        
    
    print(f"{Y}{X:02}")