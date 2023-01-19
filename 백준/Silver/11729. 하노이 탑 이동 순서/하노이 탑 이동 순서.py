## 하노이 탑 이동 순서
N = int(input())

def hanoi(n, start, pivot, end) :
    
    if n == 0 : return
    if n == 1 :
        print(start, end)
        return
    
    hanoi(n-1, start, end, pivot)
    print(start, end)
    hanoi(n-1, pivot, start, end)


def hanoi_count(n) :
    if n == 1 :
        return 1
    
    return hanoi_count(n-1) * 2 + 1

print(hanoi_count(N))
hanoi(N, 1, 2, 3)