## 종이 조각
N, M = map(int, input().split())

num_arr = [list(map(int, list(input()))) for _ in range(N)]

max_value = 0
def bitmask() :
    global max_value
    for i in range(1 << N*M ) :
        total = 0
        for row in range(N) :
            rowsum = 0
            for col in range(M) :
                # idx는 이차원 배열을 일렬로 늘렸을 때의 인덱스가 어디인지를 의미
                idx = row*M + col
                # 가로일 때
                if i & (1 << idx) != 0 :
                    rowsum = rowsum * 10 + num_arr[row][col]
                else :
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로합
        for col in range(M) :
            colsum = 0
            for row in range(N) :
                idx = row*M + col

                if i & (1<<idx) == 0 :
                    colsum = colsum * 10 + num_arr[row][col]
                else :
                    total += colsum
                    colsum = 0
            total += colsum

        max_value = max(max_value, total)


bitmask()
print(max_value)
                    
                
