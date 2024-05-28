N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)] # N+1행에 마지막 결과값들이 저장됨

dp[0][S] = 1

for idx in range(N):
	for volume in range(M+1):
		if dp[idx][volume] == 1:
			min_volume = volume - V[idx]
			max_volume = volume + V[idx]
			
			for changed_volume in [min_volume, max_volume]:
				if 0<=changed_volume<=M:
					dp[idx+1][changed_volume] = 1
			
max_volume = -1		
# N+1행에서 최댓값 탐색
for idx in range(M, -1, -1):
	if dp[N][idx] == 1:
		max_volume = idx
		break
print(max_volume)