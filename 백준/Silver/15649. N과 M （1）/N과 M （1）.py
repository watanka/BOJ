## N과 M (1)
from itertools import permutations

N, M = map(int, input().split())

for perm in permutations(range(1,N+1), M) :
    print(*perm)