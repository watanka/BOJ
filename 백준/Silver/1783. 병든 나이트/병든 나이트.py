
'''
백준 1783 병든 나이트
'''

N, M = map(int, input().split())

if N == 1:
    print(1)
    exit()

if N >= 3: #세로길이 3이상
	if M <= 6:
		max_visit = min(M, 4)
	else:
		max_visit = M - 2
else:
	max_visit = min(4, 1 + (M-1) // 2)
	
print(max_visit)