'''
백준 1931 회의실 배정
'''

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1], x[0]))


cnt = 1
end = meetings[0][1]


for i in range(1, N):
    start = meetings[i][0]
    
    if start < end:
        continue
    end = meetings[i][1]
    cnt += 1



print(cnt)