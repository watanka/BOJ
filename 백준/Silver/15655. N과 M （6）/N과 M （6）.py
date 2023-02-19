## N과 M (6)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

stack = []
def dfs(start) :
    if len(stack) == M :
        print(*stack)
        return

    for i in range(start, len(nums)) :
        if nums[i] not in stack :
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()

dfs(0)