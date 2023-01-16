## 수 정렬하기 2

N = int(input())

num_list = [int(input()) for _ in range(N)]

num_list.sort()

for num in num_list :
    print(num)