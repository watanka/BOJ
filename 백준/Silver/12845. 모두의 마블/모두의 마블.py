'''
백준 12845 모두의 마블
'''

n = int(input())

L = list(map(int, input().split()))

max_num = max(L)
max_gold = max_num * (n-2) + sum(L)

print(max_gold)