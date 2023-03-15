## 트리의 높이와 너비

N = int(input())
tree = {}

r_list = [0 for _ in range(N+1)]

for _ in range(N) :
    parent, left, right = map(int, input().split())
    tree[parent] = [left, right]
    if left != -1 :
        r_list[left] = 1
    if right != -1 :
        r_list[right] = 1

for i in range(1, N+1) :
    if r_list[i] == 0 :
        root = i

# tree[1] = [2, 3]
# tree[2] = [4, 5]
# tree[3] = [6,7]
# tree[4] = [8,-1]
# tree[5] = [9,10]
# tree[6] = [11, 12]
# tree[7] = [13, -1]
# tree[8] = [-1, -1]
# tree[9] = [14, 15]
# tree[10] = [-1, -1]
# tree[11] = [16, -1]
# tree[12] = [-1, -1]
# tree[13] = [17, -1]
# tree[14] = [-1, -1]
# tree[15] = [18, -1]
# tree[16] = [-1, -1]
# tree[17] = [-1, 19]
# tree[18] = [-1, -1]
# tree[19] = [-1, -1]
    
width = 1
visited = [[] for _ in range(N+1)]

def inorder(node, height) :
    global width
    if node != -1 :

        inorder(tree[node][0], height + 1)
        visited[height].append(width)
        width += 1
        inorder(tree[node][1], height + 1)


        


inorder(root, 1)

max_width = -1
max_level = -1
for height, coord in enumerate(visited) :
    if coord :
        if max_width < max(coord) - min(coord) + 1 :
            max_width = max(coord) - min(coord) + 1
            max_level = height
    
print(max_level, max_width)