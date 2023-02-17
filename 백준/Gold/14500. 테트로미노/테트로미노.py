## 테트로미노
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

num_arr = []
for _ in range(N) :
    num = list(map(int, input().split()))
    num_arr.append(num)

tetrominos = [
    # 1x4, 4x1
    [[1,1,1,1]], 
    [[1],[1],[1],[1]],
    # 2x2
    [[1,1], 
     [1,1]],
    # 3x2
    [[1,0],
     [1,0],
     [1,1]],

    [[1,1],
     [1,0],
     [1,0]],

    [[0,1],
     [0,1],
     [1,1]],

    [[1,1],
     [0,1],
     [0,1]],


    [[1,0],
     [1,1],
     [0,1]],

    [[0,1],
     [1,1],
     [1,0]],

    [[1,0],
     [1,1],
     [1,0]],

    [[0,1],
     [1,1],
     [0,1]],


    # 2x3
    [[1,1,1],
     [1,0,0]],

    [[1,1,1],
     [0,0,1]],

    [[1,0,0],
     [1,1,1]],

    [[0,0,1],
     [1,1,1]],

    [[1,1,0],
     [0,1,1]],

    [[0,1,1],
     [1,1,0]],

    [[1,1,1],
     [0,1,0]],

    [[0,1,0],
     [1,1,1]],
]

max_value = -1

for tet in tetrominos :
    block_h, block_w = len(tet), len(tet[0])
    for col in range(N) :
        for row in range(M) :
            if (col + block_h <= N) and (row + block_w <= M) :
                total = 0
                for h in range(block_h) :
                    for w in range(block_w) :
                        total += num_arr[col+h][row+w] * tet[h][w]

                max_value = max(max_value, total)
                

print(max_value)