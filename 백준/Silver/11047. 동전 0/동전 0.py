'''
백준 11047 동전 0
'''

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)][::-1] # 내림차순

cnt = 0
for coin in coins:
	if K >= coin:
		cnt +=  K // coin
		K %= coin
print(cnt)