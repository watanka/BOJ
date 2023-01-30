## 조합의 개수

n, r = map(int, input().split())

div2 = 0
div5 = 0

def cnt(N, div) :
    if N < div :
        return 0
    
    cnt = 0
    while N >= div :
        cnt += N // div
        N //= div
    return cnt

cnt2 = cnt(n, 2) - cnt(n-r, 2) - cnt(r, 2)
cnt5 = cnt(n, 5) - cnt(n-r, 5) - cnt(r, 5)


print(min(cnt2, cnt5))