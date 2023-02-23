## 로또


def dfs(start) :
    if len(stack) == 6 :
        print(*stack)
        return

    for i in range(start, len(num_list)) :
        if num_list[i] not in stack  :
            stack.append(num_list[i])
            dfs(i)
            
            stack.pop()

while True :
    inp = input()
    if inp == '0' :
        break
    nums = list(map(int, inp.split()))
    N = nums[0]
    num_list = nums[1:]

    stack = [] 
    dfs(0)
    print()
