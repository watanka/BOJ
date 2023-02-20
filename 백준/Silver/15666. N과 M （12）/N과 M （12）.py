## N과 M (12)

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

stack = []
def dfs(start) :
    prev = -1
    if len(stack) == M :
        print(*stack)
        return

    for i in range(start, N) :
        if nums[i] != prev :
            stack.append(nums[i])
            prev = nums[i]
            dfs(i)

            stack.pop()

dfs(0)