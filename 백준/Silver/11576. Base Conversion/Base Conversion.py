## Base Conversion
A, B = map(int, input().split())
m = int(input())
num_list_A = map(int, input().split())

dec_num = 0
for num in num_list_A :
    m-= 1
    dec_num +=  num*(A**m)

res = []
while dec_num :
    res.append(dec_num % B)
    dec_num //= B

print(*res[::-1])


