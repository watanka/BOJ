## 조세퍼스 문제
from collections import deque
N, K = map(int, input().split())
cnt = 0
q = deque(list(range(1, N+ 1)))
result = []


while len(result) < N :
    while cnt < K :
        q.append(q.popleft())
        cnt += 1

    if cnt == K :
        result.append(q.pop())
        cnt = 0

print('<' + ', '.join(map(str, result))+'>')