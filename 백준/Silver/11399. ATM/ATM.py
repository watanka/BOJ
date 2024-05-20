'''
벡준 11399반 ATM
'''

N = int(input())
P = list(map(int, input().split()))

P.sort()

wait_time = 0
answer = 0

for p in P:
    wait_time += p
    answer += wait_time

print(answer)
