stack =[]
def dfs(start) :
    if len(stack) == 6 :
        print(*stack)
        return
    for i in range(start, len(num_list)) :
        if num_list[i] not in stack :
            stack.append(num_list[i])
            dfs(i + 1)
            stack.pop()

while True :
    inp = list(map(int, input().split()))
    if inp[0] == 0 :
        break
    num_list = inp[1:]
    dfs(0)
    print()

