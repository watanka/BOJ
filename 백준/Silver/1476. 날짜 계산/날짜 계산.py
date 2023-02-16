## 날짜 계산
E, S, M = map(int, input().split())

N = 1

e,s,m = 1,1,1
while  True :
    e = N % 15 if N%15 else 15 
    s = N % 28 if N%28 else 28
    m = N % 19 if N%19 else 19
    if e == E and s == S and m == M :
        break

    N += 1

print(N)

