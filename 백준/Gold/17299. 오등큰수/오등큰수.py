## 오등큰수

N = int(input())

answer = [-1 for _ in range(N)]
nums = list(map(int, input().split()))
stack = [0]

dic = {}
for num in nums :
    if num not in dic.keys() :
        dic[num] = 1
    else :
        dic[num] += 1

for i in range(1, N) :
    while stack and (dic[nums[stack[-1]]] < dic[nums[i]]) :
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
