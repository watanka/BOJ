## Guess

N = int(input())
arr = list(input())

S = [[0]*N for _ in range(N)]

for i in range(N) :
    for j in range(i, N) :
        temp = arr.pop(0)
        if temp == '+' :
            S[i][j] = 1
        elif temp == '-' :
            S[i][j] = -1

result = [0 for _ in range(N)]


def check(idx) :
    hap = 0
    for i in range(idx, -1, -1) :
        hap += result[i]
        if hap == 0 and S[i][idx] != 0 :
            return False
        elif hap < 0 and S[i][idx] >= 0 :
            return False
        elif hap > 0 and S[i][idx] <= 0 :
            return False
    return True

def solve(idx) :
    if idx == N :
        return True
    if S[idx][idx] == 0 :
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11) :
        result[idx] = S[idx][idx] * i
        if check(idx) and solve(idx+1) :
            return True
    return False

solve(0)
print(*result)
