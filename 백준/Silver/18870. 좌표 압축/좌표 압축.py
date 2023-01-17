## 좌표 압축
import sys
N = int(input())

coords = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_coords = sorted(set(coords))

dic = {}
for i in range(len(sorted_coords)) :
    dic[sorted_coords[i]] = i

for coord in coords :
    print(dic[coord], end = ' ')
