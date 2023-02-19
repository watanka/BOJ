## N과 M (7) 
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))


stack = []
def dfs() :
    if len(stack) == M :
        print(*stack)
        return

    for num in nums :
        stack.append(num)
        dfs()
        stack.pop()


dfs()