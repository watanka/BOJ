## N과 M (9)
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

stack = []


visited = [0 for _ in range(N)]
def dfs() :
    prev = 0
    if len(stack) == M :
        print(*stack)
        return
    
    for i in range(N) :
        if not visited[i] and nums[i] != prev :
            stack.append(nums[i])
            prev = nums[i]
            visited[i] = 1
            dfs()
            stack.pop()
            visited[i] = 0


dfs()