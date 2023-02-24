## 집합
import sys
input = sys.stdin.readline
N = int(input())

status = set()

for _ in range(N) :
    inp = input().split()
    if len(inp) == 2 :
        cmd, x = inp
        x = int(x)
    elif len(inp) == 1 :
        cmd = inp[0]

    
    if cmd == 'add' :
        status.add(x)
    elif cmd == 'remove' :
        status.discard(x)
    elif cmd == 'check' :
        print(1 if x in status else 0)
    elif cmd == 'toggle' :
        if x in status :
            status.discard(x)
        else :
            status.add(x)
    elif cmd == 'all' :
        status = set(range(1, 21))
    elif cmd =='empty' :
        status.clear()




    