## 모든 순열

N = int(input())

nums = [n for n in range(1,N+1)]

stack = []
def dfs() :
    if len(stack) == N :
        print(*stack)
        return

    for i in range(N) :
        if nums[i] not in stack :
            stack.append(nums[i])
            dfs()
            stack.pop()

dfs()