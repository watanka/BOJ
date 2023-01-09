## 오븐 시계
H, M = map(int, input().split(' '))
time = int(input())

M += time

if M >= 60 :
    H += M // 60
    M = M % 60
    if H >= 24 :
        H -= 24
    print(H, M)

else :
    print(H, M)
