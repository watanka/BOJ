## 부분 수열의 합
N = input()
S = list(map(int, input().split()))

max_num = sum(S)
memory = [0 for _ in range(max_num + 1)] + [0]


def dfs(idx, val) :
    global memory
    if idx == len(S) :
        memory[val] = 1
        return

    dfs(idx+1, val+S[idx])
    dfs(idx+1, val)
    
dfs(0, 0)




num = 1
while True :
    if memory[num] :
        num += 1
    else :
        print(num)
        break