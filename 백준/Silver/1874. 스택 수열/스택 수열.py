## 스택 수열
import sys
input = sys.stdin.readline
n = int(input())

numlist = [int(input()) for _ in range(n) ]

stack = []
answer = []
push_idx = 1
flag = True
for num in numlist :

    while push_idx <= num :
        stack.append(push_idx)
        push_idx += 1
        answer.append('+')

    if stack[-1] == num :
        stack.pop(-1)
        answer.append('-')

    else :
        flag = False
        print('NO')
        break


if flag :
    for ans in answer :
        print(ans)