import sys
N = int(sys.stdin.readline())

stack = []
size = 0

for _ in range(N):
    cmdline = sys.stdin.readline().split()
    if len(cmdline) == 2:
        cmd, num = cmdline
        num = int(num)
    else:
        cmd = cmdline[0]


    if cmd == 'push':
        stack.append(num)
        size += 1
    elif cmd == 'pop':
        if size > 0:
            print(stack.pop())
            size -= 1 # size가 1이상일 때만 pop하면 size 감소
        else:
            print(-1)
        
    elif cmd == 'size':
        print(size)
    elif cmd == 'empty':
        print(0 if size > 0 else 1)
    elif cmd == 'top':
        if size > 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        raise ValueError
