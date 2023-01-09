import sys

cmds = sys.stdin.readlines()

for cmd in cmds :
    a, b = map(int, cmd.rstrip().split())
    print(a + b)