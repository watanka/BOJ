## 더하기 사이클

N = int(input())

cnt = 0

original = N


while True :
    if N < 10 :
        a = 0
        b = N
    else :
        a, b = N // 10, N % 10

    N = b*10 + ((a + b) % 10)

    
    cnt += 1
    if N == original :
        break
print(cnt)
