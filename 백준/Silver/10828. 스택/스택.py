## 스택
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N) :
    cmdline = input().split()
    
    
    if len(cmdline) == 2 :
        cmd, num = cmdline
        num = int(num)
    else : 
        cmd = cmdline[0]
    
    
    
    if cmd == 'push' :
        stack = [num] + stack
    elif cmd == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop(0))
    elif cmd == 'size' :
        print(len(stack))
    elif cmd == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif cmd == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[0])