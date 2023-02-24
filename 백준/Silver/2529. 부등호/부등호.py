## 부등호
N = int(input())
signs = [''] + list(input().split())

stack = []
min_value = 1e10
max_value = 0

def dfs(prev) :
    global min_value, max_value
    if len(stack) ==  N+1 :
        # print(*stack)
        if int(min_value) > int(''.join(map(str, stack))) :
            min_value = ''.join(map(str, stack))
        if int(max_value) < int(''.join(map(str, stack))) :
            max_value = ''.join(map(str, stack))
        
        return

    for i in range(10) :
        if i not in stack and eval(f'{prev}{signs[len(stack)]}{i}') :
            stack.append(i)
            dfs(i)
            stack.pop()

dfs(1)



print(max_value)
print(min_value)