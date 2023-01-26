## 오큰수
N = int(input())

num_list = list(map(int, input().split()))
result = [-1 for _ in range(N)]
stack = []

stack.append(0)
for i in range(1, N) :
    while stack and num_list[stack[-1]] < num_list[i] :
        result[stack.pop()] = num_list[i]
    stack.append(i)

print( *result)
