## N과 M (8)
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

stack = []
def dfs(start) :
    if len(stack) == M :
        print(*stack)
        return
    
    for i in range(start, N) :
        stack.append(nums[i])
        dfs(i)
        stack.pop()

dfs(0)
