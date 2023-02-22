## 외판원 순회 2
N = int(input())
W = []
for _ in range(N) :
    W.append(list(map(int, input().split())))

stack = []
visited = [0] * N
min_value = 10000001
def dfs(start, curr, value, stack) :
    global min_value 
    if len(stack) == N :
        if W[curr][start] :
            min_value = min(min_value, value + W[curr][start])
        return

    for i in range(N) :
        if i not in stack and W[curr][i] and value < min_value :
            stack.append(i)
            dfs(start, i, value + W[curr][i], stack)
            stack.pop()


for i in range(N) :
    dfs(i, i, 0, [i])

print(min_value)