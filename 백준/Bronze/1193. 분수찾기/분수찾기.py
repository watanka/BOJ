## 분수찾기
N = int(input())

cnt = 1
order = 0
while N - cnt > 0:
    N -= cnt
    cnt += 1

seq = list(range(1, cnt + 1))
idx = N - 1

reverse = seq[-idx-1]
right = seq[idx]

if cnt % 2 :
    print(f'{reverse}/{right}')
else :
    print(f'{right}/{reverse}')