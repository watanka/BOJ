# 벌집

N = int(input())

i = 0
add = 1
cnt = 1
while i*6 + 1 < N :
    i += add
    add += 1
    cnt += 1

print(cnt)