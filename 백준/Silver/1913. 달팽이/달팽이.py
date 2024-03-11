N = int(input())
trg_num = int(input())

if N == 1:
    print(1)
    print(1, 1)
    quit()

mid = (N - 1)//2

y, x = mid, mid
arr = [[0 for _ in range(N)] for _ in range(N)]

num = 1
arr[y][x] = num

def assign(y, x, num):
    global arr
    global trg_pos
    arr[y][x] = num

def draw(y, x, grid_size):
    global num

    # up 1
    num += 1
    y -= 1
    assign(y, x, num)
    # right grid_size - 2
    for _ in range(grid_size - 2):
        num += 1
        x += 1
        assign(y, x, num)

    # down grid_size - 1
    for _ in range(grid_size - 1):
        num += 1
        y += 1
        assign(y, x, num)

    # left grid_size - 1
    for _ in range(grid_size - 1):
        num += 1
        x -= 1
        assign(y, x, num)

    # up grid_size - 1
    for _ in range(grid_size - 1):
        num += 1
        y -= 1
        assign(y, x, num)

    return y, x



grid_size = 3
while grid_size <= N:

    y, x = draw(y, x, grid_size)
    grid_size += 2

for j in range(len(arr)):
    print(*arr[j])
    if trg_num in arr[j]:
        my = j + 1
        mx = arr[j].index(trg_num) + 1

print(my, mx)
    