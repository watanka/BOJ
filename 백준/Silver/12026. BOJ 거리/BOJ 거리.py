'''
백준 12026번 거리
'''
import sys

N = int(input())
blocks = list(input())
letters = ['B', 'O', 'J']

dp = [sys.maxsize for _ in range(N)]
dp[0] = 0
for current_ in range(N):
    cur_letter = blocks[current_]
    next_letter = letters[(letters.index(cur_letter) + 1) % 3]
    for next_ in range(current_+1, N):
        if blocks[next_] == next_letter:
            k = next_ - current_
            dp[next_] = min(dp[next_], dp[current_] + k**2)
			
print(dp[-1] if dp[-1] != sys.maxsize else -1)