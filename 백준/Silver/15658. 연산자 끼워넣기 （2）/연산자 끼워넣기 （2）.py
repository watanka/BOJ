## 연산자 끼워넣기 (2)
N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))

minval, maxval = 1e9, -1e9
def dfs(idx, total, plus, minus, mul, div) :
    global minval, maxval
    if idx == N :
        minval = min(minval, total)
        maxval = max(maxval, total)
        return

    if plus :
        dfs(idx + 1, total + nums[idx], plus-1, minus, mul, div)
    if minus :
        dfs(idx + 1, total - nums[idx], plus, minus-1, mul, div)
    if mul :
        dfs(idx + 1, total * nums[idx], plus, minus, mul-1, div)
    if div :
        dfs(idx + 1, int(total / nums[idx]), plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)
print(maxval)
print(minval)
