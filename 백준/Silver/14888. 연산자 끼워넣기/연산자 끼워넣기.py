## 연산자 끼워넣기
import sys

N = int(input())
nums = list(map(int, input().split()))
cal_list = list(map(int, input().split()))
calstr = ['+', '-', '*', '//']

maxval, minval = -1e9, 1e9


def dfs(result, plus, minus, mul, div, idx) :
    global maxval, minval
    if idx == N :
        maxval = max(maxval, result)
        minval = min(minval, result)
        return

    
    if plus :
        dfs(result + nums[idx], plus-1, minus, mul, div, idx + 1)
    if minus :
        dfs(result - nums[idx], plus, minus-1, mul, div, idx + 1)
    if mul :
        dfs(result * nums[idx], plus, minus, mul-1, div, idx + 1)
    if div :
        dfs(int(result / nums[idx]), plus, minus, mul, div-1, idx + 1)
            
plus, minus, mul, div = cal_list

dfs(nums[0], plus, minus, mul, div, 1)
print(maxval)
print(minval)
