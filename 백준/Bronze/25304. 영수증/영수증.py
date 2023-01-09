## 영수증
total = int(input())
N = int(input())

actual = 0
for _ in range(N) :
    price, num = map(int, input().split(' '))
    actual += price * num

if total == actual :
    print('Yes')
else :
    print('No')