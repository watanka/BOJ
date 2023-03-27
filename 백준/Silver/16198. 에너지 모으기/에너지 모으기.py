## 에너지 모으기
N = int(input())
nums = list(map(int, input().split()))


max_result = -1
def dfs(result, cnt, stack) :
    global max_result
    if cnt == N-2 :
        max_result = max(result, max_result)
        return

    for i in range(1, len(stack) - 1) :
        new_result = result + stack[i-1] * stack[i+1]
        pick = stack.pop(i)
        dfs(new_result, cnt + 1, stack)
        stack.insert(i, pick)
    
dfs(0, 0, nums)

print(max_result)