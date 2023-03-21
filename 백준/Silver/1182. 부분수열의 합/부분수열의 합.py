## 부분수열의 합

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
def partsum(idx, total) :
    global cnt
    if idx == N :
        return

    total += num_list[idx]
    if total == S :
        cnt += 1

    partsum(idx + 1, total )
    partsum(idx + 1, total - num_list[idx])

partsum(0, 0)

print(cnt)