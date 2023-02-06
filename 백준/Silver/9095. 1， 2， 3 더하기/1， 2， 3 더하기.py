## 1, 2, 3 더하기
T = int(input())

d = [0]*13
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12) :
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(T) :
    N = int(input())
    print(d[N])
