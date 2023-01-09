## A+B-5
import sys

while True :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == b == 0 :
        break
    print(a + b)