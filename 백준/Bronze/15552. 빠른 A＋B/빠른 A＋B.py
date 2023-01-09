## 빠른 A+B
import sys
N = int(input())

for _ in range(N) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)