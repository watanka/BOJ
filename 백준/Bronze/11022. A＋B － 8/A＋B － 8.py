## A+B - 7
import sys
N = int(input())

for i in range(N) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{i+1}: {a} + {b} = {a + b}')