N = int(input())
coord_list = [list(map(int, input().split())) for _ in range(N)]

for coord in sorted(coord_list, key = lambda x : (x[0], x[1]) ) :
    print(*coord)