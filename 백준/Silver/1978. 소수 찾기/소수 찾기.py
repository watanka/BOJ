## 소수 찾기
N = int(input())

num_list = list(map(int, input().split()))

cnt = 0

for num in num_list :
    # if num is prime number
    if num == 1 :
        continue

    prime = True
    for div in range(2, num) :
        if num % div == 0 :
            prime = False
            break
    if prime :
        cnt += 1
print(cnt)