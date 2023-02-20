## N과 M (11)
N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

stack = []
def dfs() :
    prev = 0
    if len(stack) == M :
        print(*stack)
        return

    for i in range(N) :
        if nums[i] != prev :
            stack.append(nums[i])
            prev = nums[i]
            dfs()
            stack.pop()

dfs()