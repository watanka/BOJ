## 좌표 정렬하기 2

N = int(input())
coord_list = [list(map(int, input().split())) for _ in range(N)]

for coord in sorted(coord_list, key = lambda x : (x[1], x[0]) ) :
    print(*coord)