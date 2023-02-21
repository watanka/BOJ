## 차이를 최대로
from itertools import permutations
N = int(input())
nums = list(map(int, input().split()))


def abs_sum(ls) :
    total = 0
    for i in range(len(ls)-1)  :
        total += abs(ls[i] - ls[i+1])
    
    return total

max_value = -601
for perm in permutations(nums, N) :
    max_value = max(abs_sum(perm), max_value)

print(max_value)