## 수 이어 쓰기 1

N = int(input())

i = 1
cnt = 0
while N :
    digit_standard = 9*(10**(i-1))
    if N >= digit_standard :
        cnt += i * digit_standard
        N -= digit_standard
        i += 1
    else :
        cnt += i*N
        break

print(cnt)
